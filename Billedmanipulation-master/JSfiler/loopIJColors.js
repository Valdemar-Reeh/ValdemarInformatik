function setup(){
createCanvas(600,600);
}

function draw(){
  for (let i=0;i<6;i+=1){
    for (let j=0;j<6;j+=1){
      noStroke();
      if (i==0 && j == 0){
        fill(1,1,60);
        rect(i*100,j*100,100,100);
      } else if (i==5 && j==5){
        fill(0,80,300);
        rect(i*100,j*100,100,100);
      }else{
        fill(50*i,50*j,0);
        rect(i*100,j*100,100,100);
      }
    }
  }
  noLoop();
}
background2 