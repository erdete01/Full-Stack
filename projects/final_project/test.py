import sqlite3
from flask import *
from markupsafe import escape
import os
import csv
from config import app
from models import Store, StoreSchema

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == 'POST':
            if request.form['submit_button'] == 'SignIn':
                if 'username' in session:
                    return redirect(url_for('logout'))
    
    return render_template("base.html")
    """
    try: 
        # If a user types sth on search button
        search = request.args.get("searching")
        if search:
            pass
            # return render_template("base.html", searching = search)
        # If a user enters Sign in button
        if request.method == 'POST':
            if request.form['submit_button'] == 'SignIn':
                if 'username' in session:
                    return redirect(url_for('logout'))
                return redirect(url_for('login'))
            if request.form['submit_button'] == 'myCart':
                return redirect(url_for('cart'))
            if request.form['submit_button'] == 'add':
                return redirect(url_for('cart')) 
       
        with sqlite3.connect(f"roster.db") as conn:
             conn.execute(f"drop table if exists roster")
             data = pd.read_csv(f"roster.csv", header=None)
             data.to_sql(f"roster", conn)
             # Displaying data for admin
             cur = conn.cursor()
             cur.execute(f"select * from roster")
             emptyList = []
             for name in cur:
                 name = name[1:]
                 emptyList.append(name)
             return render_template("base.html", myList=emptyList) 
        """
    

@app.route("/cart", methods=["GET", "POST"])
def cart():
    bookid = request.form.get("add") 
    bookid2 = request.form.get("add1")
    bookid3 = request.form.get("add2")
    bookid4 = request.form.get("add3")
    if bookid and bookid2 and bookid3 and bookid4:
        myList = []
        myList += [bookid]
        myList += [bookid2]
        myList += [bookid3]
        myList += [bookid4]
        myList = tuple([myList])
        return render_template("cart.html", liste=myList)  
    # value = request.form.getlist('check'):
    #     return render_template("cart.html", a = value)
    
    elif request.method == 'POST':
        if request.form['submit_button'] == 'buyItem':
            buying = request.form.get("buy")
            # value = request.form.getlist('check') 
            return render_template("cart.html", value = buying)

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
    if request.method == 'GET':
        name = request.args.get("name")
        category = request.args.get("category")
        number = request.args.get("number")
        price = request.args.get("price")
        if name and category and number and price:
            
            appendFile = open('roster.csv', 'a')
            sum = str(name) + "," + str(category) +  "," + str(number) +  "," + str(price)
            appendFile.write(sum)
            appendFile.write('\n')
            appendFile.close()

            # # Adding data to database 
            # roster = Store.query.all()
            # store_schema = StoreSchema(many=True)
            # return render_template("logout.html", roster = store_schema.dump(roster))
            

                # # Displaying data for admin
                # cur = conn.cursor()
                # cur.execute(f"select * from roster")
                # emptyList = []
                # for name in cur:
                #     name = name[1:]
                #     emptyList.append(name)
                # return render_template("logout.html", myList=emptyList)      

    if 'username' in session:
        a =  'Hello %s' % escape(session['username'])
        return render_template("logout.html", name = a)
    
    else:
        render_template("logout.html")

def read_txt(filename):
    """File format: name category number"""
    myList = []
    with open(filename, "r") as data:
        for line in data:
            myList.append(tuple(line.strip().split(", ")))
    return myList[1:]

@app.route("/remove")
def delete():
    try:
        with sqlite3.connect(f"roster.db") as conn:
                cur = conn.cursor()
                cur.execute(f"delete from roster")
                # It should also delete roster.csv file. But not finished yet. A user should first go to Costumer
                truncateFile = open('roster.csv', 'w')
                truncateFile.truncate()
                truncateFile.close()
        return redirect(url_for('logout'))
    except FileNotFoundError:
                cant = "You Can't Remove from an Empty table"
                return render_template("logout.html", myMessage=cant)
"""
@app.route("/removeSelected", methods=["GET"])
def removeDelete():

    name = request.args.get("checkRemove")
    return render_template("logout.html", hu=name)

    # """
    # try:
    #     with sqlite3.connect(f"roster.db") as conn:
    #             cur = conn.cursor()
    #             cur.execute(f"delete from roster")
    #             # It should also delete roster.csv file. But not finished yet. A user should first go to Costumer
    #             # os.remove("roster.csv") 
    #             message = "Successfully removed all the items from DB"
    #     return render_template("logout.html", myMessage=message)
    # except FileNotFoundError:
    #             cant = "You Can't Remove from an Empty table"
    #             return render_template("logout.html", myMessage=cant)
    # """

