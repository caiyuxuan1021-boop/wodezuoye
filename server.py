from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

COZE_PAT = os.getenv("COZE_PAT")  # 從 Render 的環境變數讀取
COZE_TOKEN_URL = "https://api.coze.com/open_api/auth/token"

@app.route("/coze_token", methods=["GET"])
def get_token():
    headers = {
        "Authorization": f"Bearer {COZE_PAT}"
    }
    response = requests.post(COZE_TOKEN_URL, headers=headers)
    
    if response.status_code != 200:
        return jsonify({"error": "Coze API error", "detail": response.text}), 500
    
    data = response.json()
    return jsonify({"token": data["access_token"]})

if __name__ == "__main__":
    app.run()
