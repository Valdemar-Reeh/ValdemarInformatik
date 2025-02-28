
let input;
let img;
let button;


function setup() {
  createCanvas(windowWidth,windowHeight);
  input = createFileInput(handleFile);
  input.position(200, 0);
  background(255, 0, 0);
  button = createButton('Save Image');
  button.position(19, 100);
  button.mousePressed(SAVE);
  myButton = createButton('Encrypt')
  .mousePressed(()  => pressed = true)
  .mouseReleased(() => pressed = false);
  myButton.position(100, 100);
}

function draw() {


  background(255);
  if (img) {
    image(img, 0, 0);
  }
}

function handleFile(file) {
  if (file.type === 'image') {
    img = loadImage(file.data);
    print(img.width)
  } else {
    img = null;
  }

}


function SAVE() {
    saveCanvas('myCanvas', 'jpg');
}


