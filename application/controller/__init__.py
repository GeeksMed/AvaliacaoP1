from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__, template_folder=os.path.abspath('application/view/templates'), static_folder=os.path.abspath('application/view/static'))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/videos')
def index():
    return render_template("videos.html")