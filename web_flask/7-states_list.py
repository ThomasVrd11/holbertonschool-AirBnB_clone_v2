#!/usr/bin/python3

"""j'ai la flemme de mettre un commentaira dnsjndjsdj"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """vraiment flemme"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """closing eh non je vous ai bien eu j'ai encore la flemme"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
