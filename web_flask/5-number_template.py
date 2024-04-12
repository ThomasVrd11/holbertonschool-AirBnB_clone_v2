#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def HelloHB():
    """Method that display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HB():
    """Method that display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def CText(text):
    """Method that display “C ” followed by given text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"})
def PythonText(text):
    """Method that display “Python ” followed by given text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def IsNum(n):
    """Method that display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def NumTemp(n):
    """Method that display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    # App must be listening on 0.0.0.0, port 5000
    app.run(host="0.0.0.0", port=5000)
