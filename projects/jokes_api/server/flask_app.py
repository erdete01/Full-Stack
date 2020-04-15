"""
Author: Temuulen Erdenebulgan
Instructor: Professor Roman Yasinovskyy
Class: CS330
Faker API
"""

# !/usr/bin/env python3
import random
import pyjokes
import json
from flask import Flask, request, render_template, url_for, make_response, Response, jsonify
from flask_cors import CORS, cross_origin
from faker import Faker

app = Flask(__name__)

# Returns a randon joke
@app.route("/api/v1/jokes")
def index():
    jokes = send_jokes()
    res = Response(json.dumps({"name": jokes}))
    res.headers["Access-Control-Allow-Origin"] = "*"
    res.headers["Content-Type"] = "application/json"
    return res

# Generates one joke
def send_jokes():
    content = pyjokes.get_joke()
    return content

if __name__ == "__main__":
    app.run("0.0.0.0")