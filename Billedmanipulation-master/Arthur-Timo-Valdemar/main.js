let img = loadImage('billeder/mps.jpg');
let a = 0
var falskDraw = 'false';


function preload() {
  img = loadImage('billeder/mpsFull.jpg');
}

function setup() {
  w = img.width;
  h = img.height;
  createCanvas(2 * w, h);
  noStroke();
  img.loadPixels();
}

function draw() {
  if (falskDraw == 'false'){
    img.loadImage();
    img.loadPixels();
    falskDraw = 'true';
  }

  ownFilter();
  image(img, w, 0);
  noLoop();
  background(255);
  
  image(img, w, 0);
  
}

function ownFilter() {
  for (let i = 0; i < w; i = i+1) {
    for (let j = 0; j < h; j = j+1){
      fill(getRGBvalue(0,i,j),getRGBvalue(1,i,j),getRGBvalue(2,i,j));
      rect(i, j, 1, 1);
    }
  }
}

function getRGBvalue(n,i,j){
  c = getPixelValue(n,i, j);
  if (c>160){c=255;}
  else{c=0;}
  return c;
}

function getPixelValue(n,i,j){
  p = img.pixels[(i+w*j)*4+n];
  return p;
}

