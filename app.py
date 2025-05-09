from flask import Flask, render_template
import requests

app =Flask(__name__)
@app.route("/")

def index():
    respsonse = requests.get("https://api.chess.com/pub/player/stats")
    data = respsonse.json()
    print(data)
index()