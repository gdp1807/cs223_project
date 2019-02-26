$(document).ready(function() {
  var code_width = $(".code").width();
  $(".jumbotron").css({
    'width':(code_width + 'px')
  });
});

function copy()
{
  var txt = $('.code').text();
  if(!txt || txt == '')
  {
    return;
  }
  var textArea = document.createElement("textarea");
  textArea.style.position = 'fixed';
  textArea.style.top = 0;
  textArea.style.left = 0;
  textArea.style.width = '2em';
  textArea.style.height = '2em';
  textArea.style.padding = 0;
  textArea.style.border = 'none';
  textArea.style.outline = 'none';
  textArea.style.boxShadow = 'none';
  textArea.style.background = 'transparent';
  textArea.value = txt;
  document.body.appendChild(textArea);
  textArea.select();
  try
  {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
  }
  catch (err)
  {
    console.log('Oops, unable to copy');
  }
  document.body.removeChild(textArea);
}
