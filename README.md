# digital-tribe-site

## Setup & Installation
1. Install virtualenv and create & activate virtualenv
2. ```git clone https://github.com/Bedrock02/digital-tribe-site.git```
3. ```cd digital-tribe-site;```
4. ```pip install -r requirements.txt```

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

## How to contribute
1. Create a branch off develop ```git checkout develop; git checkout -b [your-branch-name]```

2. Once you are down with your changes don't forget to rebase off develop (if needed) ```git rebase origin/develop; git push origin [your-branch-name] -f```

3. Create a pull request and notify the owner (me)