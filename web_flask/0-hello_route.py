#!/usr/bin/python3
"""Script tot start flask web"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """This method display a string"""
    return "Hello HBNB!"


@app.route("/hbnb")
def display():
    """This metthod only display HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run()
