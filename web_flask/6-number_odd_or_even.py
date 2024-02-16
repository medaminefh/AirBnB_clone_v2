#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)
# strict_slashes=False to avoid 404 error
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """
    This function returns a string when"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    This function returns a string when"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """
    This function returns a string when"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """
    This function returns a string when"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """
    This function returns a string when"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    This function returns a string when"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """
    This function returns a string when"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               n=n, odd_or_even="even")
    else:
        return render_template('6-number_odd_or_even.html',
                               n=n, odd_or_even="odd")


if __name__ == '__main__':
    # run the app on host http://0.0.0.0/ port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
