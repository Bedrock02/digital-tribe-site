import logging
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('home.html')


@app.errorhandler(500)
def server_error(e):
# Log the error and stacktrace.
  logging.exception('An error occurred during a request.')
  return 'An internal error occurred.', 500
