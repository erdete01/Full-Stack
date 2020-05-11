"""Data Model"""

from config import db, mm

# Columns of my database
class Store(db.Model):
    __tablename__ = "STORE"
    idInteger = db.Column(db.Float, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    number = db.Column(db.Integer)
    price = db.Column(db.Float)


class StoreSchema(mm.ModelSchema):
    class Meta:
        model = Store
        sqla_session = db.session



