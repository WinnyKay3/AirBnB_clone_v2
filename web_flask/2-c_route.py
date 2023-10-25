#!/usr/bin/python3
''' Start a flask web application'''

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    Routing to /hbnb, strict slashes ensure the url works
    when it ends both with or without the /'''
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
