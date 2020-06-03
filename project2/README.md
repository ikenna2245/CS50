# Project 2 SLACK: Web Programming with Python and JavaScript

The project's video: https://youtu.be/Tsw6HzTT5hQ

Application.py

This is my Python application file which renders the index.html, home.html, and chat.html file and then waits for socket events from any connected clients.

To assist with my application I imported the emit, join_room and leave_room functions of the flask socketio library, also, from werkzeug.utils import secure_filename  to help handle file upload and secure the uploaded file.  To handle the application data I declared global variables including lists for users and channels, and channel messages.
@app.route('/')
When a user visits the site the index.html page the user chooses a display name and log in.
@app.route ("/change", methods= ['POST', 'GET'])
This route handles change of display name by the user when logged in.
@app.route ("/logout")
Clears all session
@app.route("/home", methods = ['GET', 'POST'])
Renders the home.html template and list of channels created.
@app.route ("/channels/<channel>", methods = ['GET', 'POST'])
handles channel creation
@app.route ('/logout_channel')
clear channel session
@app.route('/upload_file', methods=['GET', 'POST'])
handles file upload to the server
@app.route('/download/<filename>')
handles file download from the server
@socketio.on("submit message")
When the server receives a ‘submit message’ event the message function takes the received message data (message), gets a timestamp which is then converted into a string with the format ‘HH:MM, DD Month’ and creates a new message dictionary. The new message is then appended to the nested list of message dictionaries in the messages dictionary where the key matches the channel name. If the number of messages with the key matching the channel name exceeds 100 then the pop() method is used to remove the message at the first position in the list. Finally the server emits the new message to all users in the sender’s channel.
@socketio.on ("file sent")
same function as the submit message event but for file_sent
@socketio.on ("join")
When the server receives a ‘join’ event the on_join function uses socket.io’s join_room method to add a user to a room/channel. The server then emits the joining users name to the other users on the channel to announce the join.
@socketio.on ("leave")
When the server receives a ‘leave’ event the on_leave function uses socket.io’s leave_room method to remove a user to a room/channel. The server then emits the leaving users name to the remaining users in the channel in order to announce the departure.

script.js
The file containing the client-side elements of the application (ES6), AJAX request for channel creation.

socketio.js
The web socket connection is established using the io.connect method, passing in the localhost location. and handles AJAX file upload system.

styles.css
The file containing the visual styling of the program.

layout.html
The file containing the HTML "blueprint" used by Jinja.

index.html
The file containing the HTML used for cover page of the application

home.html
(extends layout.html) for display of the created channels and to create channel and change display name.

chat.html
The file containing the HTML used for chat page and file upload

requirements.txt
The file containing the required Python libraries for the program.
