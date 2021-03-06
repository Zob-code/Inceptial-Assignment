from flask import Flask,session,redirect, url_for, escape, request
from flask import render_template
from gothonweb import planeisphere

app = Flask(__name__)

@app.route("/")
def index():
    # this is used to "set up" the session with sarting values
    session['room_name'] = planeisphere.START
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == 'GET':
        if room_name:
            room = planeisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # why is there here? do you need it?
            return render_template("You died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planeisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planeisphere.name_room(room)
            else:
                session['room_name'] = planeisphere.name_room(next_room)

        return redirect(url_for("game"))

# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'A0Zr98j/3yx R-XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run(debug=True)
