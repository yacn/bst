var inputs = document.getElementsByClassName('cart');
var total  = document.getElementById('total');
var shipping = parseFloat(document.getElementById('shipping').innerHTML);
var subtotal = 0;

function applyPayPalFee(amount) {
  var withFee = (amount * 1.029) + 0.30
  return withFee.toFixed(2)
}

for (var i=0; i < inputs.length; i++) {
  inputs[i].onchange = function() {
    var add = this.value * (this.checked ? 1 : -1);
    subtotal += add
    total.innerHTML = subtotal ? applyPayPalFee(subtotal + shipping) : 0;
  }
}
