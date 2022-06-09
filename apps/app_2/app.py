import imp
from flask import Flask
import requests
from os import environ

app = Flask(__name__)

@app.route("/")
def index():
    try:
        res = requests.get("http://" + environ["APP_1_HOST"] + ":8001")
        return "Connected to: " + res.content
    except:
        return "app_2"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8002)
