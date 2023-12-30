#!/usr/bin/python3
"""
Flask web application start page
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


def get_all(cls):
    """Function that will get all classes"""
    objects = storage.all()
    return objects


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Function that displays the main HBnB filters page
    """
    states = get_all("State")
    amenities = get_all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Tears down the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
