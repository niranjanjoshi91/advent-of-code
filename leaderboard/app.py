# pip install flask requests
# python3 app.py
# http://127.0.0.1:5000/

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your session cookie and leaderboard ID
with open("cookie.txt", "r") as f:
    cookie = f.read()

SESSION_COOKIE = cookie
BASE_URL = "https://adventofcode.com"
LEADERBOARD_ID = "121215"  # 1006803 , 121215
YEAR = 2024

def fetch_leaderboard(year, leaderboard_id):
    url = f"{BASE_URL}/{year}/leaderboard/private/view/{leaderboard_id}.json"
    cookies = {"session": SESSION_COOKIE}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.json()
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/leaderboard", methods=["POST"])
def leaderboard():
    # data = request.json
    # year = YEAR
    # leaderboard_id = LEADERBOARD_ID
    leaderboard = fetch_leaderboard(YEAR, LEADERBOARD_ID)
    if leaderboard:
        return jsonify(leaderboard)
    return jsonify({"error": "Failed to fetch leaderboard"}), 500

if __name__ == "__main__":
    app.run(debug=True)
