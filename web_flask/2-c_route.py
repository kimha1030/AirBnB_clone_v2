#!/usr/bin/python3
"""Task 2"""
from flask import Flask

app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def show_url(text):
    """Return a text"""
    text_replace = text.replace("_", " ")
    return 'C ' + str(text_replace)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
