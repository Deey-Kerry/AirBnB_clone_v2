#!/usr/bin/python3
"""
A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask("__name__")

def format_text(text):
    """underscores with space"""
    return text.replace("_", " ")

@app.route('/', strict_slashes=False)
def hello():
    """Return a string"""
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a string"""
    return ("HBNB")

@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Displays C followed by the value of the text variable"""
    return "C {}".format(format_text(text))

@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """Displays Python follow by the valus of the text variable"""
    return "Python {}".format(format_text(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
