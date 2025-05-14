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

username = "magnuscarlsen"
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