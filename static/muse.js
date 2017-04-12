
var audio;
var framePlayer;
window.onload = function(){
      initAudio();

      var clipboard = new Clipboard('.copyBtn');

      clipboard.on('success', function(e) {
          console.info('Action:', e.action);
          console.info('Text:', e.text);
          console.info('Trigger:', e.trigger);

          e.clearSelection();
      });

      clipboard.on('error', function(e) {
          console.error('Action:', e.action);
          console.error('Trigger:', e.trigger);
      });
}

function initAudio() {
    // audio = document.getElementById('player');
    // audio.src = "static/music/gen/302.mp3"
    // audio.play();
    framePlayer =document.getElementById('frame_player');
    framePlayer.src="/player";


}

function copyURL () {
  txt= "wwwwwww";
  try{

  }catch(e){
    console.log(e);
  }

}
