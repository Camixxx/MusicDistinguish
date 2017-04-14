var audio;
var framePlayer;
framePlayer =document.getElementById('frame_player');
window.onload = function(){
      initAudio();
      // var clipboard = new Clipboard('.copyBtn');
      //
      // clipboard.on('success', function(e) {
      //     console.info('Action:', e.action);
      //     console.info('Text:', e.text);
      //     console.info('Trigger:', e.trigger);
      //
      //     e.clearSelection();
      // });
      //
      // clipboard.on('error', function(e) {
      //     console.error('Action:', e.action);
      //     console.error('Trigger:', e.trigger);
      // });
}

function initAudio() {
    // audio = document.getElementById('player');
    // audio.src = "static/music/gen/302.mp3"
    // audio.play();
    framePlayer.src="/player";
    framePlayer.onload = function(){
        // alert("Local iframe is now loaded.");
        // dd = framePlayer.contentDocument;
        // tt = dd.getElementById("test_times").value;
        // tr = dd.getElementById("true_times").value;
        // console.log("total:"+tt);
        // console.log("true:"+tr);


    };
}

function testResult() {
  times = document.getElementById("checkTrue").innerText - '';
  value =  document.getElementById("checkTrue").value - '';
    if(value){
       alert("正确率为"+value*100+"%");
    }else{
        alert("多测几次才会有结果，不要点击太频繁哦。正确率每五次才会更新。")
    }
}
