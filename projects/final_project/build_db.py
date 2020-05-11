"""
It will take data from my roster, and write data into my sqlitedatabase
Only have to run this file once, unless I want to do it again
If I want to add data to do it, get data later
"""
import csv
import os
from config import db
from models import Store
def build_db(filename):
    # Delete existing DB
    if os.path.exists(f"{filename}.sqlite3"):
        os.remove(f"{filename}.sqlite3")
    # Create DB structure
    db.create_all()
    # Add data to the DB
    with open(f"{filename}.csv") as f:
        content = csv.reader(f)
        next(content)
        for line in content:
            store = Store(
                idInteger = line[0],
                name = line[1],
                category = line[2],
                number = line[3], 
                price = line[4],
            ) 
        #  add student to my database and then commit it
            db.session.add(store)
        db.session.commit()   
def main():
    build_db("roster")
if __name__ == "__main__":
    main()