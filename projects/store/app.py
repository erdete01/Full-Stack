"""
Author: Temuulen Erdenebulgan
Instructor: Professor Roman Yasinovskyy
Store Project
This project uses Sqlite Database. 
When a user enters data, it goes to roster.csv.
Then, it gets all the data from roster.csv and adds them into the database
To, make it work, a user should first check costumer.html and then can check admin.html
Deployed: 
http://tem12mka.pythonanywhere.com/
"""

import sqlite3
from flask import render_template, url_for, make_response, Flask, request
import csv
import os
import pandas as pd

app = Flask(__name__)

def read_txt(filename):
    """File format: name category number"""
    myList = []
    with open(filename, "r") as data:
        for line in data:
            myList.append(tuple(line.strip().split(", ")))
    return myList[1:]

@app.route("/")
def index():
    if request.method == "GET":
        return render_template("base.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():

    # Getting all the elements from admin.html when a user enters the number
    name = request.args.get("name")
    category = request.args.get("category")
    number = request.args.get("number")

    if name and category and number:
        sum = str(name) + "," + str(category) +  "," + str(number)
        appendFile = open('roster.csv', 'a')
        appendFile.write('\n')
        appendFile.write(sum)
        appendFile.close()

        # Adding data to database 
        with sqlite3.connect(f"roster.db") as conn:
            conn.execute(f"drop table if exists roster")
            data = pd.read_csv(f"roster.csv")
            data.to_sql(f"roster", conn)

            # Displaying data for admin
            cur = conn.cursor()
            cur.execute(f"select * from roster")
            emptyList = []
            for name in cur:
                name = name[1:]
                emptyList.append(name)
            return render_template("admin.html", name=emptyList)  
    else:
        return render_template("admin.html")

@app.route("/costumer")
def costumer():
    # Connecting to the database file
        with sqlite3.connect(f"roster.db") as conn:
                cur = conn.cursor()
                cur.execute(f"select * from roster")
                if cur:
                        emptyList = []
                        for name in cur:
                                name = name[1:]
                                emptyList.append(name)
                                return render_template("costumer.html", a=emptyList)
                text = "No DATA!"
                return render_template("costumer.html", removed=text)


# I could also remove all the data, will finish this part in the future
# Deleting Roster.csv is all I have left here. 
"""
@app.route("/remove")
def delete():
        with sqlite3.connect(f"roster.db") as conn:
                cur = conn.cursor()
                cur.execute(f"delete from roster")
                # It should also delete roster.csv file. But not finished yet. A user should first go to Costumer 
                message = "Successfully removed all the items from DB, Please Check Costumer"
        return render_template("base.html", myMessage=message)
"""






