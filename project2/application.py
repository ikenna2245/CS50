import os
import time
from time import localtime, strftime
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, flash, send_from_directory, make_response
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/static/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'zip'}

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
socketio = SocketIO(app)

users = []
channelsCreated = ["Lounge", "Coding", "Games", "CS50W"]
channelMessages = {}
timeStamp = strftime('%b-%d %I:%M%p', time.localtime())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods= ['POST','GET'])
def index():
    if "loggedin" and "currentChannel" in session:
         return redirect (url_for('enter_channel', channel = session['channel']))
    if 'loggedin'in session:
        return redirect ("/home")
    else:
        if request.method =='POST':
            user = request.form.get ("name")
            if user in users:
                if 'username' in session:
                    return redirect ("/home")
                else:
                    return render_template ('index.html', message = 'Error: Display name already in use')
            else:
                users.append(user)
                session ['username'] = user
                session ['loggedin'] = True
                session.permanent = True
                return redirect ('/home')
        return render_template ("index.html")

@app.route ("/change", methods= ['POST', 'GET'])
def change():
    if request.method == "POST":
        currentUser = session['username']
        if currentUser in users:
            num = users.index(currentUser)
            users.pop(num)
        session.pop ('username', None)
        session.pop ('loggedin', None)
        session.clear()
        newUser = request.form.get ('nameChange')
        if newUser in users:
            return render_template ('index.html', message = 'Error: Display name already in use')
        else:
            users.append(newUser)
            session ['username'] = newUser
            session ['loggedin'] = True
            session.permanent = True
            return redirect ('/home')
    else:
        if "loggedin" in session:
            return redirect ('/home')
        else:
            return redirect ('/')

@app.route ("/logout")
def logout():
    currentUser = session['username']
    if currentUser in users:
        num = users.index(currentUser)
        users.pop(num)
    session.pop ('username', None)
    session.pop ('loggedin', None)
    session.pop ('channel', None)
    session.pop ('currentChannel', None)
    session.clear()
    flash ("Goodbye, You have been Logged out")
    return redirect ("/")

@app.route("/home", methods = ['GET', 'POST'])
def home ():
    if 'loggedin' in session:
        username = session ['username']
        if request.method == 'POST':
            channel = request.form.get('channel')
            if channel not in channelsCreated:
                channelsCreated.append(channel)
                return jsonify ({"success": True})
            else:
                return jsonify ({"success":False})
        else:
            return render_template ('home.html', channels = channelsCreated, username = username)
    else:
        flash ("Choose a Display Name")
        return redirect ("/")

@app.route ("/channels/<channel>", methods = ['GET', 'POST'])
def enter_channel (channel):
    if 'loggedin' in session:
        channelName = channel
        username = session ['username']
        session['channel'] = channel
        session ['currentChannel'] = True
        session.permanent = True
        return render_template ('chat.html', channelid = channelName, userid = username, channels = channelsCreated)
    else:
        return redirect ('/')

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return jsonify ({'filedetail':True, 'error':'No selected file'})
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            res = make_response(jsonify({"message": "File uploaded"}), 200)
            return res
    return redirect ('/')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@socketio.on("submit message")
def message (data):
    message = data['message']
    username = session ['username']
    room = session.get('channel')
    emit ('announce message', {'message': message, 'username':username, 'time': timeStamp}, room=room, broadcast=True)
@socketio.on ("join")
def on_join ():
    username = session.get('username')
    room = session.get('channel')
    join_room(room)
    emit ('somedata', {"message": username + " has joined the " + room + " room."},room = room, broadcast=True)

@socketio.on ("leave")
def on_leave ():
    username = session ['username']
    room = session.get('channel')
    leave_room(room)
    emit ('somedata', {"message": username + " has left the " + room + " room."}, room = room, broadcast=True)
