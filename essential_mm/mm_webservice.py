from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

from essentialdb import EssentialDB
from weather_connector import WeatherConnector

import datetime
import random


mm_config = None
weather_connector = None
db_path = None

def _init_db():
    from quotes import initial_quotes

    with EssentialDB(filepath=db_path) as db:
        db.set("quotes", initial_quotes)


@app.route("/weather")
def weather():

    with EssentialDB(filepath=db_path) as db:
        weather = db.get("weather")
        do_update = False

        try:
            delta = datetime.datetime.now() - weather["updated"]
            if delta > datetime.timedelta(minutes=mm_config["weather"]["update_minutes"]):
                do_update = True
        except:
            #probably not an error - just no weather update yet.
            do_update = True
            pass

        if do_update:
            new_weather = weather_connector.get_weather()
            db.set("weather", new_weather)
            weather = new_weather

    return render_template("weather.html", weather=weather)


@app.route("/quote")
def quote():
    with EssentialDB(filepath=db_path) as db:
        quote = random.choice(db.get("quotes"))

    return quote

@app.route("/addmessage")
def add_message():
    return "success"

@app.route("/addquote")
def add_quote():
    return "success"

if __name__ == "__main__":

    with open('essential_mm/mm_config.json') as json_data_file:
        mm_config = json.load(json_data_file)

    weather_connector = WeatherConnector(mm_config["weather"]["url"])
    db_path = mm_config["server"]["db_file"]

    _init_db()
    app.run(mm_config['server']["interface"])
