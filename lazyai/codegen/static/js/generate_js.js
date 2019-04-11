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

function submit()
{
  var layers = document.getElementById('layers');
  var num_groups = parseInt(layers.childNodes.length) - 2;
  var group, layer = 0;
  var url = "/output/?";
  for(group = 0; group < num_groups; group++)
  {
    var grp = document.getElementById(group);
    var quad = grp.querySelectorAll('.col-md-3');
    var q;
    for(q = 0; q < 4; q++)
    {
      var form = (quad[q].childNodes)[1];
      var menu = form.childNodes[1];
      var type = menu.options[menu.selectedIndex].value;
      var num_nodes = form.childNodes[5].value;
      url += "l" + layer + "=" + type + "&" + "n" + layer + "=" + num_nodes + "&";
      layer += 1;
    }
  }
  url = window.location.host + url + "layers=" + layer + "&email=";
  window.location.href = "http://" + url;
}

function show()
{
  $("#help").toggle("medium");
  $("html, body").animate({ scrollTop:
    $("html, body").height()
  }, 800);
}
