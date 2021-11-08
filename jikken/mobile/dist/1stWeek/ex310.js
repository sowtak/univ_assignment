//アプリケーション中に使う変数を定義
var timer;
var start;
var isStarted = false;

//DOMで操作する要素を代入
var startButton = document.getElementById('start');
var stopButton  = document.getElementById('stop');
var resetButton = document.getElementById('reset');
var watch       = document.querySelector('.stopwatch p');

//イベント監視
startButton.addEventListener('click', watchStart, false);
stopButton. addEventListener('click', watchStop, false);
resetButton.addEventListener('click', watchReset, false);

//開始ボタンのイベントハンドラー
function watchStart(){
  if (! isStarted) {
    // Date() はミリ秒単位の現在時刻を出力する関数
    start = new Date();

    // setIntervalは第２引数で指定した間隔（ミリ秒単位）ごとに
    // 第１引数で指定した関数を呼び出す関数
    timer = setInterval(updateWatch, 1000/10);
    // ここでは 1/60 秒に１度 updateWatch を呼び出すと指定

    isStarted = true;
  }
}

//停止ボタンのイベントハンドラー（仕様(7)を満たすためには改造が必要）
function watchStop(){
  if ( isStarted ) {

    // clearIntervalはsetIntervalを停止する関数
    clearInterval(timer);
    isStarted = false;
  }
}

//リセットボタンのイベントハンドラー（仕様(6)を満たすためには改造が必要）
function watchReset() {
  if (!isStarted) {
    watchStop();
    watch.innerHTML = "00:00:00:0";
  }

  // DOM の watch ノードのHTML記述を更新することでゼロにリセット
}

//計測中の時刻計算用関数
function updateWatch() {
  //現在時間を date に代入
  var date = new Date();

  //ここで diff という変数を定義し、現在時刻とスタートした時刻の差分を代入
  //するコードを以下に書くこと。具体的には date と start オブジェクトの
  //getTime() メソッドの返り値を用いて計算すること。 getTime() メソッドは、
  //オブジェクト内に格納されているミリ秒単位の時刻を出力する。
  var diff = date.getTime() - start;
  var ms = Math.floor((diff % 1000)/100);
  var sec = Math.floor(diff / 1000) % 60;
  var min = Math.floor(diff / 60000);
  var hour = Math.floor(diff / 360000);

  //表示用に桁数を合わせるコードを以下に書くこと。
  if (hour < 10) hour = "0" + String(hour);
  if (min < 10) min = "0" + String(min);
  if (sec < 10) sec = "0" + String(sec);
  //DOMの watch ノードのHTML記述を書き換えることでスタートからの経過時間を
  //表示するコードを以下に書くこと。
  watch.innerHTML = hour + ":" + min + ":" + sec + ":" + ms;
}
