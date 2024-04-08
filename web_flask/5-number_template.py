#!/usr/bin/python3
""" Script that starts a Flask web application zzz"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Returns a string with a message Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a string with a message HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Shows the C and the text """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythontext(text):
    """ Shows the Python and the text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ n if n is int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ html page with n as number """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

""" cc alfredo thx for watching """
