from aiohttp import web
import json
from weather_connector import WeatherConnector
from essentialdb import EssentialDB
import random
import jinja2
import aiohttp_jinja2
import os
import datetime

class MMRequestHandler:

    def __init__(self, db_path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):

        #first, see if already exists
        if not os.path.isfile(self.db_path):
            print("creating db...")
            from quotes import initial_quotes

            with EssentialDB(filepath=self.db_path) as db:
                db.set("quotes", initial_quotes)


    @aiohttp_jinja2.template('weather.html')
    async def weather(self, request):
        with EssentialDB(filepath=self.db_path) as db:
            weather = db.get("weather")
            do_update = False

            try:
                delta = datetime.datetime.now() - weather["updated"]
                if delta > datetime.timedelta(minutes=mm_config["weather"]["update_minutes"]):
                    do_update = True
            except:
                # probably not an error - just no weather update yet.
                do_update = True
                pass

            if do_update:
                new_weather = weather_connector.get_weather()
                db.set("weather", new_weather)
                weather = new_weather

        return {'weather': weather}


    async def quote(self, request):
        with EssentialDB(filepath=self.db_path) as db:
            quote = random.choice(db.get("quotes"))

        return web.Response(text=quote)


if __name__ == "__main__":

    with open('mm_config.json') as json_data_file:
        mm_config = json.load(json_data_file)

    weather_connector = WeatherConnector(mm_config["weather"]["url"])
    db_file_path = mm_config["server"]["db_file"]

    handler = MMRequestHandler(db_file_path)

    app = web.Application()
    app.router.add_get('/weather', handler.weather)
    app.router.add_get('/quote', handler.quote)

    app.router.add_static('/static', "static")
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    web.run_app(app)



