"""
It will take data from my roster, and write data into my sqlitedatabase
Only have to run this file once, unless I want to do it again
If I want to add data to do it, get data later
"""
import csv
import os
from config import db
from models import Book, Review, Publisher
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
            #  add book info to my database and then commit it
            book = Book(
                bookID = line[0],
                bookName = line[1],
                bookAuthor = line[2],
            ) 
            #  add user info to my database and then commit it 
            review = Review(
                 isbnID = line[5],
                 averageReview = line[3],
                 ratingsCount = line[8],
            )
            #  add student to my database and then commit it 
            publisher = Publisher(
                bookID = line[0],
                isbnID = line[5],
                bookPublisher = line[11],
            )
            db.session.add(review)
            db.session.add(publisher)
            db.session.add(book)
        db.session.commit()
def main():
    build_db("books")
if __name__ == "__main__":
    main()