let img, keyImg;
var encrypted_image;
var encryptedImg;
var decryptedImg;
var encryptKey;
var updatePhoto = true;
var input;

function preload() {
  img = loadImage('billeder/tiger.jpeg'); // Original billede preloades 
}

function setup() {
  background(255, 204, 0)
  createCanvas(4 * img.width, img.height);
  noStroke();
  pixelDensity(1);
  img.loadPixels();

  input = createInput();
  input.position(0, 40 + img.height);
  input.input(updateEncryptKey); // Add event listener to save input
}

function draw() {
  if (updatePhoto && img) {
    background(255);
    imageRatio = img.width / img.height; // Finder aspect ratio for billedet så det kan vises korrekt
    image(img, 0, 0, 250 * imageRatio, 250); // Billedet der uploades skal ikke vises i fuld størrelse
    updatePhoto = false;
  }
}

//? User inputs
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

function encrypt() {
  print("Updating photo");

  // To nye billeder oprettes som kan opdateres for at gemme krypteret og dekrypteret billede
  decryptedImg = createImage(img.width, img.height);
  encryptedImg = createImage(img.width, img.height);
  
  encryptedImg.loadPixels();
  decryptedImg.loadPixels();
  
  // Loop igennem alle pixels i billedet for at kryptere og dekryptere dem
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

  image(encryptedImg, img.width, 0); // Krypteret billede vises
  image(decryptedImg, 2 * img.width, 0); // Dekrypteret billede vises
}

// Function til at opdatere nøglen ud fra en listener.
function updateEncryptKey() {
  encryptKey = int(this.value());
  encryptKeyR = encryptKey * 2;
  encryptKeyG = encryptKey * 3;
  encryptKeyB = encryptKey * 4;
}
// Function til at gemme billedet lokalt
function SAVE() {
  encryptedImg.save('encrypted_image', 'png');
  print("Image saved");
}

//? Krypteringsfunctioner 
// Function der lægger nøglen til farverne i et pixel
function encryptPixel(imgColor) {
  return color(
    (red(imgColor) + encryptKeyR) % 256,
    (green(imgColor) + encryptKeyG) % 256,
    (blue(imgColor) + encryptKeyB) % 256,
  );
}

// Function der trækker nøglen fra farverne i et pixel
function decryptPixel(encryptedColor) {
  return color(
    (red(encryptedColor) - encryptKeyR + 256) % 256,
    (green(encryptedColor) - encryptKeyG + 256) % 256,
    (blue(encryptedColor) - encryptKeyB + 256) % 256,
  );
}

