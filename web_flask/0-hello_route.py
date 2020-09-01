#!/usr/bin/python3
"""Task 0"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Index():
    """Return a str"""
    return 'Hello HBNB!'


app.run(host='0.0.0.0', port=5000)
