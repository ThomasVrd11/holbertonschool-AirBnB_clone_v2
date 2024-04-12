#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Method to display a HTML page with states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Method to display a HTML page with cities by states"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.route("/states/", defaults={"id": None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def display_states(id):
    """Displays states and cities"""
    states = storage.all(State).values()
    if id:
        state_by_id = None
        for state in states:
            if state.id == id:
                state_by_id = state
        return render_template("9-states.html", state=state_by_id, id=id)
    else:
        return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def teardown(exception):
    """Method to remove the current session"""
    storage.close()


if __name__ == "__main__":
    # App must be listening on 0.0.0.0, port 5000
    app.run(host="0.0.0.0", port=5000)
