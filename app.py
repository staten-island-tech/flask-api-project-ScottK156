from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/player_stats', methods=['GET'])
def player_stats():
    username = request.args.get('username')
    user_data = None
    error = None

    if username:
        url = f"https://api.chess.com/pub/player/{username}/stats"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
        else:
            error = f"Error: Failed to fetch data for '{username}' (status code {response.status_code})"

    return render_template('booking.html', user_data=user_data, error=error, username=username)

if __name__ == '__main__':
    app.run(debug=True)