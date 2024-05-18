#!/usr/bin/python3
"""More of the path of the url and the listening to."""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Hello."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show():
    """Hbnb."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display(text):
    """Display."""
    text = text.replace('_', ' ')
    return (f'C {text}')


@app.route("/python/", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Dynamic route."""
    text = text.replace("_", " ")
    return (f"Python {text}")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
