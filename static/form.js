function send_user(){
  name = document.getElementById('name').value;
  email = document.getElementById('email').value;
  phone = document.getElementById('number').value;
  var request = new XMLHttpRequest();
  request.open("GET", document.location.protocol + '/createuser' + '?name=' + name + '&email=' + email + '&phone=' + phone);
  request.send();
}
document.getElementById('reg').onclick = send_user();
