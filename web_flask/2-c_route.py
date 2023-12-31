#!/usr/bin/python3
"""Write script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def route_hello():
    """Return a string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def route_hbnb():
    """Returns a string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def route_cText(text):
    """display C variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
