"""
Author: Temuulen Erdenebulgan
Instructor: Professor Roman Yasinovskyy
Exercise: login 
"""

from flask import Flask, session, redirect, url_for, escape, request, render_template
import os
from markupsafe import escape

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    if 'username' in session:
        return redirect(url_for('logout'))
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('logout'))
    return render_template("login.html")
    

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == 'POST':
        session.pop('username', None)
        return redirect(url_for('index'))
    if 'username' in session:
        a =  'Hello %s' % escape(session['username'])
        return render_template("logout.html", name = a)
