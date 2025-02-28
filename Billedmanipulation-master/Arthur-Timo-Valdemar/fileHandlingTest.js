let img, keyImg;
var encrypted_image;
var encryptedImg;
var decryptedImg;
var encryptKey;
var updatePhoto = true;
var input;

function preload() {
  img = loadImage('billeder/tiger.jpeg'); // Original billede
}

function setup() {
  
  createCanvas(4 * img.width, 2 * img.height);
  
  noStroke();
  pixelDensity(1);
  img.loadPixels();
  
  //? Buttons
  buttonSave = createButton("Save Image");
  buttonSave.position(1.25 * img.width, img.height);
  buttonSave.mousePressed(SAVE);
  
  buttonEncrypt = createButton("Encrypt (in progress)");
  buttonEncrypt.position(0.25 * img.width, img.height + 20);
  buttonEncrypt.mousePressed(encrypt);

  //? Inputs
  input = createFileInput(handleFile);
  input.position(200, 0);

  input = createInput();
  input.position(0.25 * img.width, img.height);
  input.input(updateEncryptKey); // Add event listener to save input
  
}

//? File handling
function handleFile(file) {
  if (file.type === 'image') {
    img = loadImage(file.data, () => {
      img.loadPixels();
      updatePhoto = true;
    });
    print(img.width);
  } else {
    img = null;
  }
}

//? Button functions

function encrypt() {
  print("Updating photo");
  decryptedImg = createImage(img.width, img.height);
  encryptedImg = createImage(img.width, img.height);
  
  encryptedImg.loadPixels();
  decryptedImg.loadPixels();
  
  for (let i = 0; i < img.width; i++) {
    for (let j = 0; j < img.height; j++) {
      let imgColor = img.get(i, j);
  
      let encryptedColor = encryptPixel(imgColor);
      let decryptedColor = decryptPixel(encryptedColor);
  
      encryptedImg.set(i, j, encryptedColor);
      decryptedImg.set(i, j, decryptedColor);
    }
  }
  
  encryptedImg.updatePixels();
  decryptedImg.updatePixels();
  
  image(encryptedImg, img.width, 0); // Krypteret billede
  image(decryptedImg, 2 * img.width, 0); // Dekrypteret billede
}

// Function to update encryption key based on input
function updateEncryptKey() {
  encryptKey = int(this.value());
  encryptKeyR = encryptKey * 2;
  encryptKeyG = encryptKey * 3;
  encryptKeyB = encryptKey * 4;
}

function SAVE() {
  encryptedImg.save('encrypted_image', 'png');
  print("Image saved");
}

function draw() {
  if (updatePhoto && img) {
    background(255);
    imageRatio = img.width / img.height;
    image(img, 0, 0, 250 * imageRatio, 250); // Display image at smaller size
    updatePhoto = false;
  }
}

//! Kryptering

function encryptPixel(imgColor) {
  return color(
    (red(imgColor) + encryptKeyR) % 256,
    (green(imgColor) + encryptKeyG) % 256,
    (blue(imgColor) + encryptKeyB) % 256,
  );
}

function decryptPixel(encryptedColor) {
  return color(
    (red(encryptedColor) - encryptKeyR + 256) % 256,
    (green(encryptedColor) - encryptKeyG + 256) % 256,
    (blue(encryptedColor) - encryptKeyB + 256) % 256,
  );
}

