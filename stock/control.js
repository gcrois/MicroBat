var money = 10;
var buy = 30;
var sell = 30;
var stocks = 0;

var buy_slide;
var buy_disp;
var sell_slide;
var sell_disp;

var money_count;
var buy_count;
var sell_count;
var stock_count;

var mouseDown = 0;

function init() {
  // Define important values
  buy_slide  = document.getElementById("buy-drag");
  buy_disp   = document.getElementById("buy-disp");
  sell_slide = document.getElementById("sell-drag");
  sell_disp  = document.getElementById("sell-disp");

  money_count = document.getElementById("money");
  buy_count = document.getElementById("buy_order");
  sell_count = document.getElementById("sell_order");
  stock_count = document.getElementById("stocks");

  // set up events
  //buy_slide.addEventListener("mousedown", function() {adjust_buy()});
  //sell_slide.onmouseover = function() {updateMoney(--money)};

  document.body.onmousedown = function() {
    mouseDown = 1;
  }
  document.body.onmouseup = function() {
    mouseDown = 0;
  }

  buyDragEnable(buy_slide);
  sellDragEnable(sell_slide);

  updateAll();
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
}

function sell_stock(price = sell, quant = 1) {
  updateMoney(money + price * quant);
  updateStock(stocks - quant);
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
  all.style["background-image"] = "url(\"consume.gif\")";
  setTimeout( () => {
    window.location.replace("https://youtu.be/fpK36FZmTFY?t=73");
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
