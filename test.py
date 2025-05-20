""" import requests

username = "magnuscarlsen"
url = f"https://api.chess.com/pub/player/{username}/stats"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: Failed to fetch data (status code {response.status_code})")  """
import requests

username = "Scott"
url = f"https://api.chess.com/pub/player/{username}/stats"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: Failed to fetch data (status code {response.status_code})")

""" from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    error = None
    username = None

    if request.method == 'POST':
        username = request.form['username']
        url = f"https://api.chess.com/pub/player/{username}/stats"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
        else:
            error = f"Error: Failed to fetch data for '{username}' (status code {response.status_code})"

    return render_template('index.html', user_data=user_data, error=error, username=username)
if __name__ == '__main__':
    app.run(debug=True) """