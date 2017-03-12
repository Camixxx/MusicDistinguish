drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);

drop table if exists distinguish;
create table distinguish(
  id integer primary key autoincrement,
  name string not null,
  times time not null,
  type string not null,
  testtype string not null
);
