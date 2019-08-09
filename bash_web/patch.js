let count = 1;
function setup() {
  canvas = createCanvas(windowWidth - 15, windowHeight);
  canvas.position(0,0);
  canvas.style('z-index', '-2');
  gameFont = loadFont("assets/TinyPixy.ttf");
  textFont(gameFont);
  frameRate(2);
}

function draw() {
  background('#298A08');

  textSize(60);
  textAlign(LEFT, CENTER);
  // drop shadow text...
  fill(65, 255, 0);
  if ( count == 1) {
  text("$> BASHOPS.SH  ", width/2 - 223, height/2);
  count++;
  } else {
  fill(65, 255, 0);
  text("$> BASHOPS.SH_ ", width/2 - 223, height/2)
  count--;
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}
