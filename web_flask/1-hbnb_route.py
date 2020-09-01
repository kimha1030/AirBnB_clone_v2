#!/usr/bin/python3
"""Task 1"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Index():
    """Return a str"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def Hbnb():
    """Return a str"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
