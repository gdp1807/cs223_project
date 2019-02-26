function duplicate()
{
  var layers = document.getElementById('layers');
  var id = parseInt(layers.childNodes.length) - 3;
  var group = document.getElementById(id);
  group.setAttribute('class', 'carousel-item');
  var clone = group.cloneNode(true);
  clone.id = ++id;
  clone.setAttribute('class', 'carousel-item active');
  var quad = clone.querySelectorAll('.col-md-3');
  quad[0].setAttribute('id', id.toString() + ".1");
  quad[1].setAttribute('id', id.toString() + ".2");
  quad[2].setAttribute('id', id.toString() + ".3");
  quad[3].setAttribute('id', id.toString() + ".4");
  group.parentNode.appendChild(clone);
  var ul = layers.getElementsByTagName('li');
  for(var i = 0; i < ul.length; i++)
  {
    if(ul[i].hasAttribute('class'))
      ul[i].removeAttribute('class');
  }
  var li = document.createElement("li");
  li.setAttribute('data-target', '#carouselExampleIndicators');
  li.setAttribute('data-slide-to', id);
  li.setAttribute('class', 'active');
  layers.appendChild(li);
}

function show()
{
  $("#help").toggle("medium");
  $("html, body").animate({ scrollTop:
    $("html, body").height()
  }, 800);
}
