

from flask import Flask, render_template, request 
import requests

app = Flask(__name__)

chess_com_usernames = [
    "MagnusCarlsen",
    "DanielNaroditsky",
    "lachesisQ",
    "DingLiren",
    "akaNemsko",
    "GothamChess",
    "AnnaCramling",
    "EricRosen",
    "GMBenFinegold",
    "chessbrah",
    "AnishGiri",
    "AlirezaFirouzja",
    "LeQuangLiem",
    "IndianLad",
]

@app.route('/')
def index():
    return render_template('index.html', usernames=chess_com_usernames)

@app.route('/player_stats')
def player_stats():
    username = request.args.get('username')
    user_data = None
    error = None

    if username:
        url = f"https://api.chess.com/pub/player/{username}/stats"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        try:
            response = requests.get(url, headers=headers) 
            response.raise_for_status()
            try:
                user_data = response.json()

            except ValueError:
                error = "Error: Failed to parse response JSON."

        except requests.exceptions.RequestException as e:
            error = f"Request error: {e}"

    return render_template('booking.html', user_data=user_data, error=error, username=username)

if __name__ == '__main__':
    app.run(debug=True)