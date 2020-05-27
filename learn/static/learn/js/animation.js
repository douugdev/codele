function retract(id) {
  document.getElementById('card' + id).setAttribute("class", "card retracted");
  document.getElementById('card' + id).onmousedown = function () {
    expand(id);
  }
}

function expand(id)
{
  document.getElementById('card' + id).setAttribute("class", "card");
  document.getElementById('card' + id).onmousedown = function () {
    retract(id);
  }
}
