# rdb - Vue.js GUI for pulling data from reddit with praw

#### This project is an exploration of Vue, flask and various related modules for educational purposes. The idea was to look more closely at how to create modern web-based GUI-s for some python scripts I had lying around.

#### rdb lists submissions of a specified subreddit, lets you select the ones you're interested in and then by pressing "Grab data" shows some collected data in a table with some charts to go with it.

- backend: flask
- frontend: Vue.js with vue-material

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
(Windows)
mkdir backend (in project folder root)
cd backend
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
```

### Running flask and node

```
cd ..
cd frontend
npm install
npm run dev
cd ..
flask run

(Situational: manually set environment variables)
FLASK_APP=run.py
FLASK_DEBUG=1

PowerShell:
$env:FLASK_APP="run.py"
$env:FLASK_DEBUG=1
```
