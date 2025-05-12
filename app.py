from flask import Flask, render_template
import requests

app =Flask(__name__)
@app.route("/")


def get_chess_com_stats(username):
    url = f"https://api.chess.com/pub/player/{username}/stats"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch stats for {username}. Status code: {response.status_code}")
        return None

# Example usage
username = "GMNaroditsky"
stats = get_chess_com_stats(username)

if stats:
    print("Rapid Rating:", stats.get("chess_rapid", {}).get("last", {}).get("rating"))
    print("Blitz Rating:", stats.get("chess_blitz", {}).get("last", {}).get("rating"))
    print("Bullet Rating:", stats.get("chess_bullet", {}).get("last", {}).get("rating"))