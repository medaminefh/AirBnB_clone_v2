#!/usr/bin/python3
"""
This script starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)
# strict_slashes=False to avoid 404 error
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    """
    This function returns a string when"""
    return "Hello HBNB!"


if __name__ == '__main__':
    # run the app on host http://0.0.0.0/ port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
