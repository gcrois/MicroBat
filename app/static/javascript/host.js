var start_button;
var xhttp;

function init() {
  xhttp = new XMLHttpRequest();
  start_button = document.getElementById("start_button");

  xhttp.open("GET", "host", true);
  xhttp.send();

  console.log("hi");
}
