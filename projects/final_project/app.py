"""
Author: Temuulen Erdenebulgan
Instructor: Professor Roman Yasinovskyy
Description: Final Project
http://tfinal.pythonanywhere.com/home
"""

import sqlite3
from flask import *
from markupsafe import escape
import os
import csv
from config import app
from models import *
from build_db import *
import random
import requests

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Base Template
@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/home", methods=["GET", "POST"])
def home():
    try:            
        if request.form['submit_button'] == 'myList':
            return redirect(url_for('login'))
        if request.form['submit_button'] == 'moreInfo':
            return redirect(url_for('moreInfo'))
    except:
        with sqlite3.connect(f"roster.sqlite3") as conn:
            cur = conn.cursor()
            # From 3 tables, I want to select only bookName, averageReview, ratingsCount, and bookPublisher
            cur.execute(f"select bookName, averageReview, ratingsCount, bookPublisher from BOOKNAME, \
                BOOKPUBLISHER, BOOKREVIEW where BOOKNAME.bookID = BOOKPUBLISHER.bookID and BOOKREVIEW.isbnID \
                = BOOKPUBLISHER.isbnID")
            emptyList = []
            # Appending them to an emptyList. Since Appending is Constant Time. I believe it should not take so much time
            for name in cur:
                emptyList.append(name)
            return render_template("home.html", roster=emptyList)   

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('logout'))
    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    try:
        if request.form['submit_button'] == 'out':
            session.pop('username', None)
            return redirect(url_for('home')) 
        if request.form['submit_button'] == 'delete':
            truncateFile = open('shopping.csv', 'w')
            truncateFile.truncate()
            truncateFile.close()
            return redirect(url_for('logout'))
    except: 
        # Getting all the values when a user enters values  
        bookname = request.args.get("bookname")
        comment = request.args.get("comment")
        if bookname and comment:
            appendFile = open('shopping.csv', 'a')
            sum =  str(bookname) + "," + str(comment)
            appendFile.write(sum)
            appendFile.write('\n')
            appendFile.close()
            with open("shopping.csv", "r") as f:
                content = f.read().split('\n')
                return render_template("logout.html", aaa=content)
        else:    
            if 'username' in session:
                a =  'Hello %s' % escape(session['username'])
                return render_template('logout.html', greetings = a) 
            return render_template("logout.html")
