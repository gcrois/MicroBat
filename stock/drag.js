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
  buy_slide.addEventListener("mousedown", function() {adjust_buy()});
  sell_slide.onmouseover = function() {updateMoney(--money)};

  document.body.onmousedown = function() {
    mouseDown = 1;
  }
  document.body.onmouseup = function() {
    mouseDown = 0;
  }

  updateAll();
}

function adjust_buy(e = window.event) {
  console.log(Math.round(getY(e) / document.documentElement.clientHeight * 100));
  updateBuy(100 - Math.round(getY(e) / document.documentElement.clientHeight * 100));
  setTimeout( () => {
    if (mouseDown == 1) {
      adjust_buy(e);
    }
  }, 100);
}

function set_sell(value) {
  sell_disp.style['height']      = value + 'vh';
  sell_slide.style['margin-top'] = 'calc(' + value + 'vh - 10vh)';
}

function set_buy(value) {
  buy_disp.style['height']      = value + 'vh';
  buy_disp.style['margin-top']  = (100 - value) + 'vh';
  buy_slide.style['margin-top'] = 'calc(' + (100 - value) + 'vh)';
}

function updateMoney(val = money){
  money_count.innerHTML = "$" + val;
}

function updateBuy(val = buy){
  buy_count.innerHTML = "$" + val;
  set_buy(val);
}

function updateSell(val = sell){
  sell_count.innerHTML = "$" + val;
  set_sell(val);
}

function updateStock(val = stocks){
  stock_count.innerHTML = val;
}

function updateAll(){
  updateStock();
  updateBuy();
  updateSell();
  updateMoney();
}

function getY(e) {
	var posy = 0;
	if (!e) var e = window.event;
	if (e.pageY) 	{
		posy = e.pageY;
	}
	else if (e.clientY) 	{
		posy = e.clientY + document.body.scrollTop
			+ document.documentElement.scrollTop;
	}
  return posy;
}
