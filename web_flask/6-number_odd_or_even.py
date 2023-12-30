#!/usr/bin/python3
"""
Flask Module
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """display C text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """display Python text variable"""
    txt = text.replace("_", " ")
    return "Python {}".format(txt)


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """display “n is a number” """
    if isinstance(n, int):
        return "{} is a number".format(n)


def render_no_template(n, template):
    """display a HTML page if it renders no template
    """
    if isinstance(n, int):
        return render_template(template, n=n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display a HTML number template"""
    return render_no_template(n, "5-number.html")


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """displays a HTML page only if its odd or even
    """
    if isinstance(n, int):
        if n % 2:
            eo = "odd"
        else:
            eo = "even"
        return render_template("6-number_odd_or_even.html", n=n, eo=eo)


if __name__ == "__main__":
    app.run()
