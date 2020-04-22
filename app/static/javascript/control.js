// important per-user variables
var money = 10;
var buy = 30;
var sell = 30;
var stocks = 0;
var time = 5;
var clock = 0;

// utility variables for dragging / interaction
var buy_slide;
var buy_disp;
var sell_slide;
var sell_disp;
var sub_button;
var sub_field;
var intro_msg;

// amount displayed
var money_count;
var buy_count;
var sell_count;
var stock_count;
var timer;

var mouseDown = 0;

var lose;
var understand;

// clock loop
var clock_interval;

function init() {
  // Set all element variables
  intro_msg = document.getElementById("instructions");
  sub_button = document.getElementById("submit");
  sub_field = document.getElementById("name");

  buy_slide  = document.getElementById("buy-drag");
  buy_disp   = document.getElementById("buy-disp");
  sell_slide = document.getElementById("sell-drag");
  sell_disp  = document.getElementById("sell-disp");

  money_count = document.getElementById("money");
  buy_count = document.getElementById("buy_order");
  sell_count = document.getElementById("sell_order");
  stock_count = document.getElementById("stocks");
  timer = document.getElementById("timer");

  lose = new sound("media/audio/you-lose.wav");
  understand = new sound("media/audio/high-level.wav");

  // set up events
  document.body.onmousedown = function() {
    mouseDown = 1;
  }
  document.body.onmouseup = function() {
    mouseDown = 0;
  }
  sub_button.onclick = function(){user_start()};

  updateAll();
}


//================================================================//
// User input gathered to start game
//================================================================//
function user_start() {
  understand.play();

  move_letter();

  buyDragEnable(buy_slide);
  sellDragEnable(sell_slide);

  // start clock
  let d = new Date();
  clock = d.getTime();
  clock_interval = setInterval(function(){ clock_count(); }, 100);
}

function move_letter(progress = 1) {
  intro_msg.style["margin-top"] = (3.5 - (progress / 60 * 83.5)) + "vh";
  if (progress == 60) {
    intro_msg.style["display"] = "none";
  }
  else {
    setTimeout(() => {
      move_letter(++progress);
    }, 30);
  }
}

//================================================================//
// Changes visual slider for buy and sell order
//================================================================//
function set_sell(value) {
  sell_disp.style['height']      = value + 'vh';
  sell_slide.style['margin-top'] = 'calc(' + value + 'vh - 10vh)';
}

function set_buy(value) {
  buy_disp.style['height']      = value + 'vh';
  buy_disp.style['margin-top']  = (100 - value) + 'vh';
  buy_slide.style['margin-top'] = 'calc(' + (100 - value) + 'vh)';
}


//================================================================//
// Changes visual slider for buy and sell order
//================================================================//
function purchase(price = buy, quant = 1) {
  updateMoney(money - price * quant);
  updateStock(stocks + quant);

  stock_count.style["color"] = "yellow";
  setTimeout(() => { stock_count.style["color"] = "black";}, time * 1000);
}

function sell_stock(price = sell, quant = 1) {
  updateMoney(money + price * quant);
  updateStock(stocks - quant);

  money_count.style["color"] = "yellow";
  setTimeout(() => { money_count.style["color"] = "black";}, time * 1000);
}


//================================================================//
// Sets readout to appropriate value rounded to the right precision
// If parameter is given, set value
//================================================================//
function updateMoney(val = money){
  money = val;
  money_count.innerHTML = "$" + val.toFixed(2);
}

function updateBuy(val = buy){
  buy = val;
  buy_count.innerHTML = "$" + val.toFixed(2);
  set_buy(val);
}

function updateSell(val = sell){
  sell = val;
  sell_count.innerHTML = "$" + val.toFixed(2);
  set_sell(val);
}

function updateStock(val = stocks){
  stocks = val;
  stock_count.innerHTML = val.toFixed(0);
}

function setTime(val = time) {
  time = val;
  timer.innerHTML = val.toFixed(1);
}

function clock_count() {
  var d = new Date();
  let diff = (d.getTime() - clock) / 1000;
  clock = d.getTime();
  if ((time - diff) < .05) {
    tick();
    clearInterval(clock_interval);
  }
  else {
    setTime(Math.max(time - diff, -99.9));
  }
}

function tick() {
  // reset clock
  setTime(Math.max(5, -99.9));

  // check lose condition
  if (money <= 0) {
    consume();
  }

  // wait for backend response
  setTimeout(() => {
    var d = new Date();
    clock = d.getTime();
    clock_interval = setInterval(function(){ clock_count(); }, 100);
  }, 1000);
}


//================================================================//
// Update all readouts to current stored values
//================================================================//
function updateAll(){
  updateStock();
  updateBuy();
  updateSell();
  updateMoney();
}

//================================================================//
// Triggers consumption overlay and redirects page
//================================================================//
function consume() {
  let all = document.getElementById("overall");
  all.style.display = "block";
  all.style["background-image"] = "url(media/images/consume.gif)";
  console.log(all.style);
  lose.play();
  setTimeout( () => {
    window.location.href = "https://www.merriam-webster.com/dictionary/loser";
  }, 4840);
}


//================================================================//
// DRAGGING FUNCTIONS - followed example from
// https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_draggable
//================================================================//
function buyDragEnable(elmnt) {
  var cursorY = 0, newLoc = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    cursorY = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    cursorY = e.clientY;
    // set the element's new position:
    newPrice = 100 - ((cursorY) / window.innerHeight) * 100;
    // move both if adjacent
    if (newPrice > (100 - sell)) {
      // check that we aren't hiding sell
      if ((100 - newPrice) > 5) {
        updateBuy(newPrice);
        updateSell(100 - newPrice);
      }
      else {
        updateBuy(95);
        updateSell(5);
      }
    }
      // otherwise, just adjust buy
      else {
        if (newPrice > 5) {
          updateBuy(newPrice);
        }
        else {
          updateBuy(5);
        }
      }
    }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

function sellDragEnable(elmnt) {
  var cursorY = 0, newLoc = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    cursorY = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    cursorY = e.clientY;
    // set the element's new position:
    newPrice = ((cursorY) / window.innerHeight) * 100;
    // move both if adjacent
    if (newPrice > (100 - buy)) {
      // check that we aren't hiding sell
      if ((100 - newPrice) > 5) {
        updateSell(newPrice);
        updateBuy(100 - newPrice);
      }
      else {
        updateBuy(5);
        updateSell(95);
      }
    }
      // otherwise, just adjust buy
      else {
        if (newPrice > 5) {
          updateSell(newPrice);
        }
        else {
          updateSell(5);
        }
      }
    }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

//================================================================//
// Audio player (from https://www.w3schools.com/graphics/game_sound.asp)
//================================================================//
function sound(src) {
  this.sound = document.createElement("audio");
  this.sound.src = src;
  this.sound.setAttribute("preload", "auto");
  this.sound.setAttribute("controls", "none");
  this.sound.style.display = "none";
  document.body.appendChild(this.sound);
  this.play = function(){
    this.sound.play();
  }
  this.stop = function(){
    this.sound.pause();
  }
}
