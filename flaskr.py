# -*- coding: utf-8 -*-
# all the imports
import os
import sqlite3,time
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, json
# create our little application :)
app = Flask(__name__)

#### Database ###
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='0000'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    """Initializes the database."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


#### Url ###
@app.route('/')
def index():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)

@app.route('/player')
def player():
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()

    path1 = os.getcwd() +'/static/music/gen'
    path2 = os.getcwd() +'/static/music/raw'
    list1 = os.listdir(path1)
    list2 = os.listdir(path2)
    variable={"gen":list1,"raw":list2,}
    print(os.getcwd())
    return render_template('player.html',variable=variable)

@app.route('/en')
def show_entries():
    db = get_db()
    cur = db.execute('select id, name, type, testtype ,times from distinguish order by id desc')
    entries = cur.fetchall()
    print(entries)
    # log = db.execute('select name, ')
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/distinguish',methods=['POST'])
def distinguish():
    error = None
    db = get_db()
    data={'times':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}
    #name,times,type,testtype
    for kv in request.data.split( '&' ):
        args = kv.split('=')
        data[args[0]] = args[1]

    db.execute('insert into distinguish (name,times,type,testtype) values (?, ?, ?, ?)',
                 [data['name'], data['times'], data['type'],data['testtype']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('player'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()
