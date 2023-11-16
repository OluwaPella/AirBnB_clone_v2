#!/usr/bin/python3
""" module """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ def """
    return 'HELLO HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """def """
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def inter(text):
    """ replc with a whitespace """
    formatted_text = text.replace("_", " ")
    return "C {}".format(formatted_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
