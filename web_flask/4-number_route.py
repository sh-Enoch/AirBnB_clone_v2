#!/usr/bin/python3


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def show():
    return "HBNB"


@app.route("/python/<string: name>", strict_slashes=False)
def python(name="is_cool"):
    return "Python %s" % (name).replace("_", " ")


@app.route("/number/<n: integer>", strict_slashes=False)
def number(n):
    return "%d is a number" % (n)


if __name__ == "__main__":
    app.run(debug=True, host=0.0.0.0.0, port=5000)
