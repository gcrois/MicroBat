let row = 0;
function makeColor() {
  var imageData = context.getImageData(0, 0, canvas.width, canvas.height);
  for (var i = 0; i < imageData.width; i++) {
    setPixel(imageData, i, row, 255, 100, 0);
  }
  context.putImageData(imageData, 0, 0);
  row++;
}


/* takes image, position, and color data and sets image pixel */
function setPixel(data, x, y, r, g, b, a = 255) {
  let loc = (x + y * data.width) * 4;
  data.data[loc + 0] = r;
  data.data[loc + 1] = g;
  data.data[loc + 2] = b;
  data.data[loc + 3] = a;
}


function init() {
  canvas = document.getElementById('Canvas');
  context = canvas.getContext('2d');
  canvas.width = 500;
  canvas.height = 500;
}
