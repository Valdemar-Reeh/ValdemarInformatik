function setup(){
  createCanvas(windowWidth, windowWidth);
}

function draw(){
  noStroke()
  for (let i=0;i<windowWidth;i+=1){
    for (let j=0;j<windowWidth;j+=1){
      fill(0.5*(i-j),0.5*(j-i),255-Math.abs((i-j))*0.5)
      rect(i,j,1,1);
    }
  }
  noLoop();
}
