#!/usr/bin/python3

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route that displays "Hello HBNB!"."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that displays "HBNB"."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text='is_cool'):
    """Route that displays "C ", followed by the value of the text variable."""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    """Route displays "Python ", followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
