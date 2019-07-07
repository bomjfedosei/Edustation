function poisk(ser){
  var request = new XMLHttpRequest();
  request.open("GET", document.location.protocol + '/search/' + ser)
  request.send()
  request.onload = function(){
    JSON.parse(request.responseText);
    tor = JSON.parse(request.responseText);
    document.getElementsByClassName('main_content')[0].innerHTML = '';
    for (var key in tor){
      string = '<div class="cart">' + '<div class="img_wrap">' + '<img src="static/' + tor[key]['image'] + '" alt="photo">';
      string += '</div><a href="/card/' + tor[key]['page_title'] + '">' + '<h2>' + tor[key]['title'] + '</h2></a>';
      string += '<div class="cart_info"><ul>';
      string += '<li class="cart_teacher">'+ tor[key]['school'] + '</li>';
      string += '<li class="cart_time">' + tor[key]['duration'] + ' месяцев</li>';
      string += '<li>' + tor[key]['type'] + '</li>';
      string += '<li>' + tor[key]['price'] + ' руб</li>';
      string += '</ul></div><p>' + tor[key]['description'] + '</p></div>'
      document.getElementsByClassName('main_content')[0].innerHTML += string;
    }
  }
}
