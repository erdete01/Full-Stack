""""App Config File"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Flask app
app = Flask(__name__)
this_dir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(this_dir, "roster.sqlite3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO"] = True

#DB Object
db = SQLAlchemy(app)

#Marshmallow Object
mm = Marshmallow(app)