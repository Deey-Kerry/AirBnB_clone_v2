#!/usr/bin/python3
"""
Flask application projects
"""

from flask import Flask, render_template
from models import storage
from models.state import state
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """tears down the storage on teardown"""
    storage.close()

@app.route('/states', strict_slashes=False)
def state():
    """Function that displays a html page with states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<state_id>', strict_slashes=False)
def state_by_id(id):
    """function that displays the states and cities
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
