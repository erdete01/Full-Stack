import sqlite3
from flask import *
from markupsafe import escape
import os
import csv
from config import app
from models import Store, StoreSchema
from build_db import *
import random

pp = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return redirect(url_for('home'))

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'add':
            # Add this to a list and create a new csv file
            bookit = request.form.get("add") 
            bookit2 = request.form.get("add1")
            bookit3 = request.form.get("add2")
            bookit4 = request.form.get("add3")
            appendFile = open('shopping.csv', 'a')
            sum = str(bookit) + "," + str(bookit2) +  "," + str(bookit3) +  "," + str(bookit4)
            appendFile.write(sum)
            appendFile.write('\n')
            appendFile.close()

        if request.form['submit_button'] == 'SignIn':
            if 'username' in session:
                return redirect(url_for('logout'))
            return redirect(url_for('login'))
        if request.form['submit_button'] == 'myCart':
            return redirect(url_for('cart'))
        search = request.args.get("searching")
        if search:
            pass
    try:
        greetings = "Dear Costumer, we have following items"
        roster = Store.query.all()
        store_schema = StoreSchema(many=True)
        return render_template("home.html", roster=store_schema.dump(roster), greetingss = greetings)
    except:
        greetings = "Dear Costumer, we are broke :("
        return render_template("home.html", greetingss = greetings)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('logout'))
    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():

    if request.method == 'POST':
        # Removes an item from database when a user clicks remove button
        if request.form['submit_button'] == 'remove':
            removeSelected = request.form.get("removeSelected") 
            removeSelected2 = request.form.get("removeSelected2")
            removeSelected3 = request.form.get("removeSelected3")
            removeSelected4 = request.form.get("removeSelected4")
            with sqlite3.connect(f"roster.sqlite3") as conn:
                cur = conn.cursor()
                if removeSelected:
                    cur.execute(f"delete from STORE where name=?", (removeSelected, ))
                    # Updating CSV File, when removed from the database
                    lines = []
                    with open('roster.csv', 'r') as readFile:
                        reader = csv.reader(readFile)
                        for row in reader:
                            lines.append(row)
                            for field in row:
                                if field == removeSelected:
                                    lines.remove(row)
                    with open('roster.csv', 'w') as writeFile:
                        writer = csv.writer(writeFile)
                        writer.writerows(lines)
        # When a user clicks LogOut Button, it logs out.
        if request.form['submit_button'] == 'out':
            session.pop('username', None)
            return redirect(url_for('home'))

    # Getting all the values when a user enters values    
    name = request.args.get("name")
    category = request.args.get("category")
    number = request.args.get("number")
    price = request.args.get("price")
    randomNumber = random.randrange(0, 10100, 2)
    
    # Adding all the values to the database and csv file
    if name and category and number and price:
        appendFile = open('roster.csv', 'a')
        sum =  str(randomNumber) + "," + str(name) + "," + str(category) +  "," + str(number) +  "," + str(price)
        appendFile.write(sum)
        appendFile.write('\n')
        appendFile.close()

        build_db('roster')
        roster = Store.query.all()
        store_schema = StoreSchema(many=True)
        return render_template("logout.html", roster=store_schema.dump(roster))
    
    # Greets the username and logs out when clicked
    if 'username' in session:
        a =  'Hello %s' % escape(session['username'])
        try:
            roster = Store.query.all()
            store_schema = StoreSchema(many=True)
            return render_template("logout.html", roster=store_schema.dump(roster), name = a)
        except:
            return render_template("logout.html", name = a)

    return render_template("logout.html")

@app.route("/cart", methods=["GET", "POST"])
def cart():
        
        with open('shopping.csv', 'r') as readFile:
            
            file_contents = readFile.read()
            readFile.close()
        a = tuple([file_contents.split()])
        return render_template("cart.html", liste=a)

    # value = request.form.getlist('check'):
    #     return render_template("cart.html", a = value)
    # if request.method == 'POST':
    #     if request.form['submit_button'] == 'buyItem':
    #         buying = request.form.get("buy")
    #         # value = request.form.getlist('check') 
    #         return render_template("cart.html", value = buying)

@app.route("/remove")
def delete():
    try:
        with sqlite3.connect(f"roster.sqlite3") as conn:
                cur = conn.cursor()
                cur.execute(f"delete from STORE")
                # It should also delete roster.csv file. But not finished yet. A user should first go to Costumer
                truncateFile = open('roster.csv', 'w')
                truncateFile.truncate()
                truncateFile.close()
                appendFile = open('roster.csv', 'a')
                sum = "idInteger,name,category,number,price"
                appendFile.write(sum)
                appendFile.write('\n')
                appendFile.close()
        return redirect(url_for('logout'))
    except FileNotFoundError:
                cant = "You Can't Remove from an Empty table"
                return render_template("logout.html", myMessage=cant)