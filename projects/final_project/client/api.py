"""

Persistent API : http://untii.pythonanywhere.com/api/v1/name

"""


import json
from flask import Flask, Response, jsonify
import random

app = Flask(__name__)
# CORS(app)
@app.route("/api/v1/name")
def get_name():
    movie_names = [
        "Harry Potter and the Half-Blood Prince", "Harry Potter and the Order of the Phoenix",
        "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban",
        "Harry Potter Boxed Set  Books 1-5", "Harry Potter Collection (Harry Potter  #1-6)",
        "The Ultimate Hitchhiker's Guide: Five Complete Novels and One Story (Hitchhiker's Guide to the Galaxy  #1-5)",
        "The Ultimate Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy  #1-5)",
        "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy  #1)",
        "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy  #1)",
        "The Ultimate Hitchhiker's Guide (Hitchhiker's Guide to the Galaxy  #1-5)",
        "A Short History of Nearly Everything",
        "Bill Bryson's African Diary",
        "Bryson's Dictionary of Troublesome Words: A Writer's Guide to Getting It Right",
        "In a Sunburned Country",
        "I'm a Stranger Here Myself: Notes on Returning to America After Twenty Years Away",
        "The Lost Continent: Travels in Small Town America",
        "Neither Here nor There: Travels in Europe",
        "Notes from a Small Island",
        "The Mother Tongue: English and How It Got That Way",
        "J.R.R. Tolkien 4-Book Boxed Set: The Hobbit and The Lord of the Rings",
        "The Lord of the Rings (The Lord of the Rings  #1-3)",
        "The Fellowship of the Ring (The Lord of the Rings  #1)",
        "The Lord of the Rings (The Lord of the Rings  #1-3)",
        "The Lord of the Rings: Weapons and Warfare",
        "The Lord of the Rings: Complete Visual Companion",
        "Agile Web Development with Rails: A Pragmatic Guide",
        "Hatchet (Brian's Saga  #1)",
    ]
    random_name = random.choice(movie_names)
    res = Response(json.dumps
    ({
        "name": random_name,
    }))
    res.headers["Access-Control-Allow-Origin"] = "*"
    res.headers["Content-Type"] = "application/json"
    return res
    

if __name__ == "__main__":
    app.run("0.0.0.0")