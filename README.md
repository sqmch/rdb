# rdb - Vue.js GUI for pulling data from reddit using praw (WIP)

#### Demo: https://rdb.netlify.com/

- backend: Flask
- frontend: Vue.js

##### This project is an exploration of Vue and python for learning purposes. The idea was born from interest in creating modern web-based GUI-s for python scripts. The chosen implementation of that idea was to create a platform for exploring reddit data using it's API.

##### The underlying idea of the practice project is to give the user different ways to explore subreddit/submission data. Currently the ways data is to be explored using the app are basic and a work in progress.

##### Original inspiration for how to combine flask with Vue.js: https://github.com/oleg-agapov/flask-vue-spa

## Setup

### praw authentication

- create a praw.ini file in the project root directory with the following inside:

```
[bot1]
client_id=YOURCLIENTID
client_secret=YOURCLIENTSECRET
password=YOURPASSWORD
username=YOURUSERNAME
```

- make a reddit account and 'create app' (script)
- you will get the client_id and client_secret while creating the app
- update praw.ini with the new details and save
- The name in brackets on the first line ('bot1' by default) has to match the argument passed to praw.Reddit in rdb.py

### Make a virtual env and install dependencies

```
(windows)
mkdir backend (in project folder root)
cd backend
python -m venv venv
venv/scripts/activate
cd ..
pip install -r requirements.txt

(linux)
mkdir backend (in project folder root)
cd backend
virtualenv -p python3 venv
source venv/bin/activate
cd ..
pip3 install -r requiremenets.txt
```

### Running flask and node

```
cd frontend
npm install
npm run dev
cd ..
flask run

(Situational: set environment variables)
PowerShell:
$env:FLASK_APP="run.py"
$env:FLASK_DEBUG=1

Bash:
export FLASK_APP=run.py
export FLASK_DEBUG=1
```
