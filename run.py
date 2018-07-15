# vue/flask implementation of rcdbot (some simpimport requests
import requests
from flask import Flask, render_template, jsonify
from random import *

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")


@app.route("/api/random")
def random_number():
    response = {"randomNumber": randint(1, 100)}
    return jsonify(response)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    """[asdasd asda dsa sdasdasd]

    Arguments:
        path {[type]} -- [description]
    """

    if app.debug:
        return requests.get("http://localhost:8084/{}".format(path)).text
    return render_template("index.html")
