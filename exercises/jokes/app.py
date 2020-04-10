"""
Author: Temuulen Erdenebulgan
Instructor: Professor Roman Yasinovskyy
Class: CS330
"""

# !/usr/bin/env python3
import random
import pyjokes
from flask import Flask, request, render_template, url_for, make_response

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def index():
    # Getting all the numbers from form.html when a user enters the number
    language = request.args.get("language")
    category = request.args.get("type")
    number = request.args.get("number")

    # if language and category and number exists, it will run line 15
    if language and category and number:
        myNumber = int(number)
        jokes = send_jokes(language=language, category=category, number=myNumber)
        numbersOfJokes = str(jokes[0:myNumber]).strip('[]')
        return render_template("form.html", joke=numbersOfJokes)
    
    # When a user opens the page, it will directly call form.html
    else: 
        return render_template("form.html")

# generate jokes based on language and category
def send_jokes(language : str, category : str, number : int):
    content = pyjokes.get_jokes(language, category)
    return content

