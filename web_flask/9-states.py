#!/usr/bin/python3
"""Task 6"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Function that return states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_states(id):
    """Function that return states"""
    states = storage.all(State).values()
    vals = None
    for s in states:
        if id in s.id:
            vals = s
            ban = 1
            break
        else:
            ban = 0
    return render_template('9-states.html', vals=vals)


@app.teardown_appcontext
def close_session(db):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
