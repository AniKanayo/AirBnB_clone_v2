#!/usr/bin/python3
"""A script that starts a Flask web application:
the web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
The use of option strict_slashes=False in the route definitionis must"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
