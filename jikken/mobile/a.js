var color_id = 0; // 0は初期色の白を示している
var max_colors = 10;

var colors = new Array(max_colors);
colors[0] = "#ffffff"; // colors[0]は必ず白とすること
colors[1] = "#ffff00"; // 黄色
colors[2] = "#0000ff"; // 青色
colors[3] = "#ff00ff"; // pink
colors[4] = "#00ff00"; // lightgreen
colors[5] = "#0ff0ff"; // lightblue
colors[6] = "#f0f0f0"; // pink
colors[7] = "#fedacb"; // brown
colors[8] = "#aaff00"; // yellow
colors[9] = "#f0f0ff"; // baige
function changeBgForward() {
  if(color_id<max_colors) {
    color_id=color_id+1;
    document.body.style.backgroundColor(colors[color_id]);
  } else document.body.style.backgroundColor(colors[max_colors-1]);
}

function changeBgBackward() {
  if(color_id>0) {
    color_id=color_id-1;
    document.body.style.backgroundColor(colors[color_id]);
  } else document.body.style.backgroundColor(colors[0]);
}

window.addEventListener("load",  function(e) {
  var forward = document.getElementById("forward");
  var backward = document.getElementById("backward");

  forward.addEventListener("click", changeBgForward, false);
  backward.addEventListener("click", changeBgBackward, false);
}, false);