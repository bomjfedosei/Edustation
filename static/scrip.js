function response(type) {
  var request = new XMLHttpRequest();
  var typetext = '';
  if (type == 'all'){
    typetext = "/dial";
    request.onload = function() {
      console.log(JSON.parse(request.responseText));
    }
  }
  request.open("GET", document.location.protocol + "/dial");
  request.send()
}
