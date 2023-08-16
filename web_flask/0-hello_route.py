#!/usr/bin/python3
"""
simple Flask app that listens for requests at root URL
It displays the message “Hello HBNB!”
It listens to 0.0.0.0, port 5000
"""

import os
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns a string "Hello HBNB!"
    When routed
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
