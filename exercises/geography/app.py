#!/usr/bin/env python3
import requests
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for
import records

app = Flask(__name__)

def get_data(host: str, port: int, user: str, dbname: str, query: str) -> list:
    db = records.Database(f"postgres://{user}:@{host}:{port}/{dbname}")
    rows = db.query(query)
    return rows


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("base.html")
    if request.form.get("country"):
        country = request.form.get("country")
        result = get_data(
            host="localhost",
            port=2345,
            user="erdete01",
            dbname="world",
            query=f"select *, city.name as capitalname from country left join city on country.capital = city.id where code = '{country}';",
        )
        return render_template("result.html", rows=result.all())

    if request.form.get("region"):
        region = request.form.get("region")
        result = get_data(
            host="localhost",
            port=2345,
            user="erdete01",
            dbname="world",
            query=f"select *, city.name as capitalname from country left join city on country.capital = city.id where region = '{region}';",
        )
        return render_template("result.html", rows=result.all())


    if request.form.get("continent"):
        continent = request.form.get("continent")
        result = get_data(
            host="localhost",
            port=2345,
            user="erdete01",
            dbname="world",
            query=f"select *, city.name as capitalname from country left join city on country.capital = city.id where continent = '{continent}';",
        )
        return render_template("result.html", rows=result.all())

@app.route("/<string:scope>", methods=["GET"])
def search(scope: str):
    if scope == "country":
        THE_WORLD = get_data(
            host="localhost",
            port=2345,
            user="erdete01",
            dbname="world",
            query="select code, name from country;",
        )
        return render_template("country.html", options=THE_WORLD)

    elif scope == "region":
        # get regions from the database and populate options of the drop-down menu
        THE_WORLD = get_data(
            host="localhost",
            port=2345,
            user="erdete01",
            dbname="world",
            query="select distinct region from country;",
        )
        return render_template("region.html", options=THE_WORLD)

    elif scope == "continent":
        # get continents from the database and populate options of the drop-down menu
        THE_WORLD = get_data(
            host="localhost",
            port=2345,
            user="erdete01",
            dbname="world",
            query="select distinct continent from country;",
        )
        return render_template("continent.html", options=THE_WORLD)

if __name__ == "__main__":
    app.run()


