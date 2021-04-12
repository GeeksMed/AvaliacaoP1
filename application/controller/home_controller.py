from application import app
from flask import Flask, render_template, request, url_for

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/videos')
def videos():
    return render_template("videos.html")