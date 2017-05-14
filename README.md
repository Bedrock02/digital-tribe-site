# digital-tribe-site

## Setup & Installation
1. Install virtualenv
2. ```git clone https://github.com/Bedrock02/digital-tribe-site.git```
3. ```cd digital-tribe-site; workon (environment created in step 1)```
4. ```pip install -r requirements.txt```
5. npm install

## Run Project Locally
1. ```export FLASK_APP=main.py```
2. ```flask run```
At this point you should see something like....
```
* Serving Flask app "main"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [29/Mar/2017 19:31:30] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [29/Mar/2017 19:31:30] "GET /favicon.ico HTTP/1.1" 404 -
```
3. Navigate to http://127.0.0.1:5000/ and you should see the app running in your browser

## Adding Sass styles
1. Install Sass (http://sass-lang.com/install)
2. Add or modify sass styles
3. ```sass --watch main.scss:main.css --style compressed``` (For making style changes)

## Adding Javascript files
1. Add or modify js files and add CommonJS module syntax
2. ```browserify static/js/main.js > static/js/dist/bundle.js```