import os
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "hello"


@app.route('/2')
def second():
    return "endpoint 2"


@app.route('/3', methods=['POST'])
def third():
    return "endpoint 2"
