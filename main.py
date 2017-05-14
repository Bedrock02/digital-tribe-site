import logging
from flask import Flask
from flask import render_template
from helpers.header_data import header_data

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html', nav_item=0, header_data=header_data['home'])

@app.route('/about-us.html')
def about():
  return render_template('about-us.html', nav_item=1, header_data=header_data['about'])

@app.route('/services.html')
def contact():
  return render_template('services.html', nav_item=2, header_data=header_data['services'])

@app.route('/contact-us.html')
def services():
  return render_template('contact-us.html', nav_item=3, header_data=header_data['contact'])

@app.errorhandler(500)
def server_error(e):
# Log the error and stacktrace.
  logging.exception('An error occurred during a request.')
  return 'An internal error occurred.', 500

@app.errorhandler(404)
def server_not_found(e):
  logging.exception('Page not found')
  return "Oops, you have left the Tribe, the page you are looking for doesn't exist", 404