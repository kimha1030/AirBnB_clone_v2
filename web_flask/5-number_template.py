#!/usr/bin/python3
"""Task 5"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Index():
    """Function index"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def Hbnb():
    """Function hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """Function show text C"""
    text_replace = text.replace("_", " ")
    return 'C ' + str(text_replace)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='is_cool'):
    """Function show text python"""
    text_replace = text.replace("_", " ")
    return 'Python ' + str(text_replace)


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """Function show number"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_template(n):
    """Function show template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
