from flask import Flask, render_template
import requests

app =Flask(__name__)
@app.route("/")


def get_chess_com_stats():

    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)