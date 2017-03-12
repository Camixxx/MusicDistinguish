
var audio;
var framePlayer;
window.onload = function(){
      initAudio();
}

function initAudio() {
    // audio = document.getElementById('player');
    // audio.src = "static/music/gen/302.mp3"
    // audio.play();
    framePlayer =document.getElementById('frame_player');
    framePlayer.src="/player";
}
