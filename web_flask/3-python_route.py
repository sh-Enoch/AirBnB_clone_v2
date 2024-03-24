#!/usr/bin/python3
"""web application listening to host 0.0.0.0 at port 5000"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Route: /
    Description: Displays "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route: /hbnb
    Description: Displays "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text='is_cool'):
    """
    Route: /c/<text>
    Description: Displays "C " followed by the value of the text variable
    (replace underscore _ symbols with a space).
    Default value of text is "is_cool".
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    """
    Route: /python/<text>
    Description: Displays "Python " followed by the value of the text variable
    (replace underscore _ symbols with a space).
    Default value of text is "is_cool".
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
