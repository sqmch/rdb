# rdb - pull data from reddit

- backend: flask, praw
- frontend: vue.js with vue-material

#

### make a virtual env and install dependencies

```
mkdir backend (in project folder root)

cd backend
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
```

### running flask and node

```
cd ..
cd frontend
npm install
npm run dev
cd ..
$env:FLASK_APP="run.py"
$env:FLASK_DEBUG=1
flask run
```

### praw authentication

- create a praw.ini file in the project root directory with the following inside:

```
[bot1]
client_id=YOURCLIENTID
client_secret=YOURCLIENTSECRET
password=YOURPASSWORD
username=YOURUSERNAME
```

- make a reddit account and 'create app' (script) at https://www.reddit.com/prefs/apps

- you will get the client_id and client_secret from creating the app

- update praw.ini and save

- praw will now read auth information from the ini file, keep in mind the name in the brackets ('bot1' in this case) has to match the argument passed to praw.Reddit in rdb.py
