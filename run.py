# vue/flask implementation of rcdbot (some simpimport requests
import requests
from flask import Flask, render_template, jsonify
from random import *
from rdb import Rdb

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")


@app.route("/api/submissions")
def serve_submissions():
    rdb = Rdb()
    data = rdb.get_submissions()
    return jsonify(data)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if app.debug:
        return requests.get("http://localhost:8081/{}".format(path)).text
    return render_template("index.html")
