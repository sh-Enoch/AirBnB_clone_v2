#!/usr/bin/python3
"""more of the path of the url and the listening to """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display(text):
    text = text.replace('_', ' ')
    return (f'C {text}')

@app.route("/python/", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return (f"Python {text}")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
