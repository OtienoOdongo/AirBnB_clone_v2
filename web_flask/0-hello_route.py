#!/usr/bin/python3
#A simple Flask app that listens for requests at root and displays the message “Hello HBNB!”
#It listens to 0.0.0.0, port 5000

import os
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

