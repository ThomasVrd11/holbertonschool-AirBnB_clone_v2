#!/usr/bin/python3
""" Script that starts a Flask web application zzz"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Returns a string with a message Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a string with a message HBNB"""
    return "HBNB"


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

""" cc alfredo thx for watching """
