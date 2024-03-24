#!/usr/bin/python3
"""web application listening to port 0.0.0.0.0 port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB"


@app.route("/hnbn", strict_slashes=False)
def show():
    return "HBNB"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is_cool'):
    return "python" + text.replace('_', " ")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
