#!/usr/bin/python3
""" aaaaaaaaaaaa"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ closing """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ states id"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state, id=True)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')