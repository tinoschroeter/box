var host = 'ws://localhost:9091/';
var socket;          // the websocket
var sensorValue = 0; // the sensor value

function setup() {
  createCanvas(windowWidth, windowHeight);
  // connect to server:
  socket = new WebSocket('ws://' + host);
  // socket connection listener:
  // socket.onopen = sendIntro;
  // socket message listener:
  socket.onmessage = readMessage;
}

function draw() {
  background("#00BFFF");
  fill(255,255 * sensorValue,0);
  ellipse( width / 2, height / 2 * sensorValue, 100);

  fill(255);
  textSize(50);
  text(sensorValue + ' load auf inventar.zeit.de', width / 2 - 300, height / 2 - 60);
  text('mit WebSockets.', width / 2 - 300, height / 2)

  fill(244,164,96);
  rect(width / 500, height / 1 - 60, width, height, 20);
}

function sendIntro() {
  // convert the message object to a string and send it:
  // socket.send("Hello");
}

function readMessage(event) {
  var msg = event.data; // read data from the onmessage event
  sensorValue = Number(msg);
  // println(sensorValue); // print it
}
