#!/usr/bin/python3
"""
A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask("__name__")

def format_text(text):
    """Displays a format text"""
    return text.replace("_", " ")


@app.route('/', strict_slashes=False)
def hello():
    """Return a string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display C text variable"""
    return "C {}".format(format_text(text))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_Text(text="is cool"):
    """display Python text variable
    """
    return "Python {}".format(format_text(text))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """displays a number"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
