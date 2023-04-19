import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    result_json = {
        "hi": "hello",
        "hello": "hi"
    }
    return jsonify(result_json)
