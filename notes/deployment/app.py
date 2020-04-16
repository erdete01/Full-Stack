"""
Author: Temuulen Erdenebulgan
Instructor: Professor Roman Yasinovskyy
Class: CS330
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
def index() :
    jokes = send_joke()
    res = Response(json.dumps({"name": jokes}))
    res.headers["Access-Control-Allow-Origin"] = "*"
    res.headers["Content-Type"] = "application/json"
    return res

# Generates a random joke
def send_joke() :
    content = pyjokes.get_joke()
    return content

# Returns a specific joke based on the number
# If the ID is greater than the number of jokes in the collection,
# It returns the last joke from the list

@app.route("/api/v1/jokes/<int:n>")
@cross_origin()
def get_nth_numberOfJokes(n) :
    jokes = sendJokes()
    n = int(n)
    try:
        numberOfJokes = str(jokes[n]).strip('[]')
    except IndexError:
        numberOfJokes = str(jokes[-1]).strip('[]')
    return jsonify(name=numberOfJokes)

# Generates multiple jokes
def sendJokes() :
    content = pyjokes.get_jokes()
    return content

if __name__ == "__main__":
    app.run("0.0.0.0")
