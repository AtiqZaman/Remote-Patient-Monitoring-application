import boto3
import cv2
from flask import Flask, render_template, Response
from camera import VideoCamera
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator

app = Flask(__name__)
nav = Nav(app)

nav.register_element('ny_navbar', Navbar('TheNave',View('Home', 'Doctor') ))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/doctor")
def doctor():
    return render_template("doctor.html")

@app.route("/family")
def family():
    return render_template("family.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

@app.route("/KVSmediaViewer")
def KVSmediaViewer():
    return render_template("KVSmediaViewer.html")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)