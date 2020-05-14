"""Data Model"""

from config import db, mm
# Columns of my database
class Book(db.Model):
    __tablename__ = "BOOKNAME"
    bookID = db.Column(db.Integer, primary_key=True)
    bookName = db.Column(db.String)
    bookAuthor = db.Column(db.String)

class Review(db.Model):
    __tablename__ = "BOOKREVIEW"
    isbnID = db.Column(db.Integer, primary_key=True)
    averageReview = db.Column(db.Float)
    ratingsCount = db.Column(db.Integer)

class Publisher(db.Model):
    __tablename__ = "BOOKPUBLISHER"
    bookID = db.Column(db.Integer, primary_key=True)
    isbnID = db.Column(db.Integer)
    bookPublisher = db.Column(db.String)

class BookSchema(mm.ModelSchema):
    class Meta:
        model = Book
        sqla_session = db.session

class ReviewSchema(mm.ModelSchema):
    class Meta:
        model = Review
        sqla_session = db.session

class PublisherSchema(mm.ModelSchema):
    class Meta:
        model = Publisher
        sqla_session = db.session
