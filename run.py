# vue/flask implementation of rcdbot (some simpimport requests
import requests
from flask import Flask, render_template, jsonify
from rdb import Rdb


app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
rdb = Rdb()


@app.route("/api/submissions")
def search_submissions():
    search_results = rdb.get_submissions()
    return jsonify(search_results)


@app.route("/api/process_selections", methods=['GET', 'POST'])
def process_selections():
    response_object = {}
    if request.method == 'POST':
        selected_subs = request.get_json()
        response_object = rdb.scan_submissions(selected_subs)
    else:
        response_object['placeholder'] = 'if request.method==POST failed'
    return jsonify(response_object)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if app.debug:
        return requests.get("http://localhost:8081/{}".format(path)).text
    return render_template("index.html")
