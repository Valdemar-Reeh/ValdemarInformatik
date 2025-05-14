
function vissang(){
  x = Math.floor(Math.random()*3);
  console.log(x );
  var song = data[x];
  
  console.log(data[x]);
  document.getElementById('songs').innerHTML = song;

  const iframe = document.getElementById('myIframe');
  iframe.src = data[x].SRC;
}



window.onload = function() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "data.csv", true);
  xhr.responseType = "text";
    xhr.onload = function() {
    data = Papa.parse(xhr.responseText, {
      header: true // set this to true if the first row contains the header names
    }).data;
    };
  xhr.send();
}
