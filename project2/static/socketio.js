// Get a reference to the progress bar, wrapper & status label
var progress = document.getElementById("progress");
var progress_wrapper = document.getElementById("progress_wrapper");
var progress_status = document.getElementById("progress_status");

// Get a reference to the 3 buttons
var upload_btn = document.getElementById("upload_btn");
var loading_btn = document.getElementById("loading_btn");
var cancel_btn = document.getElementById("cancel_btn");

// Get a reference to the alert wrapper
var alert_wrapper = document.getElementById("alert_wrapper");

// Get a reference to the file input element & input label
var input = document.getElementById("file_input");
var file_input_label = document.getElementById("file_input_label");

function show_alert(message, alert) {
  alert_wrapper.innerHTML = `
    <div id="alert" class="alert alert-${alert} alert-dismissible fade show" role="alert">
      <span>${message}</span>
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    `
  }

  function input_filename() {
    file_input_label.innerText = input.files[0].name;
  }
  // Function to reset the page
  function reset() {
    // Clear the input
    input.value = null;
    // Hide the cancel button
    cancel_btn.classList.add("d-none");
    // Reset the input element
    input.disabled = false;
    // Show the upload button
    upload_btn.classList.remove("d-none");
    // Hide the loading button
    loading_btn.classList.add("d-none");
    // Hide the progress bar
    progress_wrapper.classList.add("d-none");
    // Reset the progress bar state
    progress.setAttribute("style", `width: 0%`);
    // Reset the input placeholder
    file_input_label.innerText = "Select file";
  }


document.addEventListener ('DOMContentLoaded', ()=>{
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  socket.on ('connect', ()=>{
      socket.emit('join');
  });

  socket.on('connect', () => {
    document.querySelector ('#submitChat').onclick = () => {
      const message = document.querySelector('#chatArea').value;
        if (document.querySelector('#chatArea').value == "") {
          document.querySelector ('#submitChat').disable = "True";
        } else {
          socket.emit('submit message', {"message":message});
        }
    };
  });

  socket.on ('connect', ()=>{
    document.querySelector('#upload_btn').onclick = ()=>{
      if (!input.value) {
        show_alert("No file selected", "warning")
        return;
      }
      // Create a new FormData instance
      var data = new FormData();
      // Create a XMLHTTPRequest instance
      var request = new XMLHttpRequest();
      // Clear any existing alerts
      alert_wrapper.innerHTML = "";
      // Disable the input during upload
      input.disabled = true;
      // Hide the upload button
      upload_btn.classList.add("d-none");
      // Show the loading button
      loading_btn.classList.remove("d-none");
      // Show the cancel button
      cancel_btn.classList.remove("d-none");
      // Show the progress bar
      progress_wrapper.classList.remove("d-none");
      // Get a reference to the file
      var file = input.files[0];
      // Get a reference to the filename
      var filename = file.name;
      // Get a reference to the filesize & set a cookie
      var filesize = file.size;
      document.cookie = `filesize=${filesize}`;
      // Append the file to the FormData instance
      data.append("file", file);
      // request progress handler
      request.upload.addEventListener("progress", function (e) {
        // Get the loaded amount and total filesize (bytes)
        var loaded = e.loaded;
        var total = e.total
        // Calculate percent uploaded
        var percent_complete = (loaded / total) * 100;
        // Update the progress text and progress bar
        progress.setAttribute("style", `width: ${Math.floor(percent_complete)}%`);
        progress_status.innerText = `${Math.floor(percent_complete)}% uploaded`;
      })
      // request load handler (transfer complete)
        request.addEventListener("load", function (e) {
          const data = JSON.parse (request.responseText);
          var data1 = data.filename;
          var data2 = data.link;
          if (request.status == 200) {
            show_alert(`File uploaded`, "success");
            socket.emit('file sent', {'filename':data1, 'link':data2});
          }
            else {
              show_alert(`Error uploading file`, "danger");
            }
            reset();
          });

          // request error handler
          request.addEventListener("error", function (e) {
            reset();
            show_alert(`Error uploading file`, "warning");
          });

          // request abort handler
          request.addEventListener("abort", function (e) {
             reset();
             show_alert(`Upload cancelled`, "primary");
           });

          // Open and send the request
          request.open("post", '/upload_file');
          request.send(data);

          cancel_btn.addEventListener("click", function () {
          request.abort();
          })
    };
  });

  socket.on('announce message', data => {
    const li = document.createElement('li');
    li.innerHTML= `
    <div class="list-group">
      <div class="list-group-item list-group-item-action">
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">${data.username}</h5>
          <small>${data.time}</small>
        </div>
          <p class="mb-1">${data.message}</p>
      </div>
    </div> `;
    document.querySelector('#chats').append(li);
    document.querySelector('#chatArea').value='';
  });

  socket.on('announce file', data => {
    const li = document.createElement('li');
    li.innerHTML= `
    <div class="list-group">
      <div class="list-group-item list-group-item-action">
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">${data.username}</h5>
          <small>${data.time}</small>
        </div>
          <p class="mb-1"><a href="${data.link}"> ${data.filename}</a></p>
      </div>
    </div> `;
    document.querySelector('#chats').append(li);
  });

  socket.on('somedata', data => {
    const li = document.createElement('li');
    li.innerHTML = `
    <div class="list-group">
      <div class="list-group-item list-group-item-action">
        <div class="d-flex w-100 justify-content-between">
          <h6 class="mb-1">${data.message}</h6>
        </div>
      </div>
    </div>
    `;
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
