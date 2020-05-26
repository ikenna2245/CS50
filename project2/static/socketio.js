document.addEventListener ('DOMContentLoaded', ()=>{
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  socket.on ('connect', ()=>{
      socket.emit('join');
  });

  socket.on('connect', () => {
    document.querySelector ('#submitChat').onclick = () => {
      const message = document.querySelector('#chatArea').value;
        if (document.querySelector('#chatArea').value == "") {
          document.querySelector ('#submitChat').disable = True;
        } else {
          socket.emit('submit message', {"message":message});
        }
    };
  });

  socket.on('announce message', data => {
    const li = document.createElement('li');
    li.innerText= `${data.time}>>> ${data.username} - ${data.message}`;
    document.querySelector('#chats').append(li);
    document.querySelector('#chatArea').value='';
  });

  socket.on('somedata', data => {
    const li = document.createElement('li');
    li.innerHTML = data.message;
    document.querySelector('#chats').append(li);
  });

  document.querySelector('#leave').addEventListener('click', ()=>{
    socket.emit('leave')
    window.location.replace('/home')
  });
  document.querySelectorAll('.select-room').forEach((li) => {
    li.onclick = ()=> {
      socket.emit ('join');
    }
  });
  document.querySelector('#chatArea').addEventListener("keydown", event => {
              if (event.key == "Enter") {
                  document.getElementById("submitChat").click();
              }
          });
});
