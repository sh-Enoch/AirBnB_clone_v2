#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Route that displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route that displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Route that displays 'C ' followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Route displays 'Python ' followed by the value of the text variable
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Route that displays 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Route that displays an HTML page with 'Number: n' if n is an integer"""
    if isinstance(n, int):
        return render_template('number.html', number=n)
    else:
        return "Not a valid number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
