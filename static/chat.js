var count_message = 0;
function get_dialog(msg, data){
  var message = msg;
  if (count_message == 0){
    message = '1';
  }
  var request = new XMLHttpRequest();
  request.open("GET", document.location.protocol + "/dialog/" + message + '?back=' + data);
  request.send()
  request.onload = function(){
    tor = JSON.parse(request.responseText);
    if (data != undefined){
      document.getElementsByClassName('msg_history')[0].innerHTML += '<div class="outgoing_msg"><div class="sent_msg"><p>' + data + '</p></div></div>';
    }
    document.getElementsByClassName('msg_history')[0].innerHTML += '<div class="incoming_msg"><div class="received_msg"><div class="received_withd_msg"><p>' + tor['bot'].dialog + '</p></div></div></div>';
    document.getElementsByClassName('variable')[0].innerHTML = '';
    for (var element in tor){
      if (element != 'bot'){
        if (tor[element].dialog == '(Name)'){
          document.getElementById('sender').onclick = function(){
            message = document.getElementById('writer').value;
            get_dialog('7', message);
          }
        }
        else{
          document.getElementsByClassName('variable')[0].innerHTML += '<button class="msg_variable_btn" onclick="get_dialog('+ "'" + tor[element].id + "', '"+ tor[element].dialog + "'" + ')" type="button">'+ tor[element].dialog +'</button>';
        }
      }
    }
    count_message++;
  };
}
get_dialog()
