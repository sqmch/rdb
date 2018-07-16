# make a virtual env and install dependencies

mkdir backend (in project folder root)

cd backend

python -m venv venv

venv/scripts/activate

pip install requirements.txt

# running flask and node

cd ..

cd frontend

npm run dev

cd ..

$env:FLASK_APP="run.py"

$env:FLASK_DEBUG=1

flask run
