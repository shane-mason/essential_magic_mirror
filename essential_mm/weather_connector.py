import requests
import datetime

class WeatherConnector:

    def __init__(self, url):
        self.url = url

    def get_weather(self):
        try:
            r = requests.get(self.url)
            d = r.json()

            (icon_path, weather_description) = self._make_description_icon(d["weather"][0]["icon"])
            temp_description = self._make_temp_description(int(d["main"]["temp"]), int(d["wind"]["speed"]))
            weather = {
                "updated": datetime.datetime.now(),
                "humidity": int(d["main"]["humidity"]),
                "temp": int(d["main"]["temp"]),
                "wind": int(d["wind"]["speed"]),
                "condition": d["weather"][0]["main"],
                "condition_code": d["weather"][0]["id"],
                "description": d["weather"][0]["description"],
                "icon": d["weather"][0]["icon"],
                "icon_path": icon_path,
                "weather_description": weather_description,
                "temp_description": temp_description,
                "status": True
            }
        except Exception as e:
            print("Error getting weather...")
            print(e)
            weather = {
                "updated": datetime.datetime.now(),
                "status": False,
            }

        return weather


    def _make_description_icon(self, icon):

        description = ""
        icon_path = ""
        if icon == "01d.png" or icon == "02n.png":
            description = "Clear skies"
            icon_path = "sun.png"
        elif icon.startswith("02") or icon.startswith("03"):
            description = "Partly cloudy"
            icon_path = "partyly-cloudy.png"
        elif icon.startswith("04") or icon.startswith("09") or icon.startswith("10"):
            description = "Rainy"
            icon_path = "cloud.png"
        elif icon.startswith("50"):
            description = "Misty"
            icon_path = "cloud.png"
        elif icon.startswith("11"):
            description = "Thunderstorms"
            icon_path = "thunder.png"
        elif icon.startswith("13"):
            description = "Snow"
            icon_path = "thunder.png"
        else:
            description = "I don't know what's going on out there..."
            icon_path = "sun.png"

        hour = datetime.datetime.now().hour

        if hour <= 5:
            description += " this late night."
        elif hour <= 10:
            description += " this morning."
        elif hour <= 13:
            description += " today."
        elif hour <= 17:
            description += " this afternoon."
        elif hour <= 19:
            description += " this evening."
        else:
            description += " tonight."

        return(icon_path, description)

    def _make_temp_description(self, temp, wind):

        if temp < 30:
            description = "It's freeeezing"
        elif temp < 40:
            description = "It's really cold"
        elif temp < 50:
            description = "It's cold"
        elif temp < 60:
            description = "It's cool"
        elif temp < 70:
            description = "It's coolish"
        elif temp < 80:
            description = "It's nice"
        elif temp < 90:
            description = "It's warm"
        else:
            description = "It's hot"

        if wind > 35:
            description += " &amp super windy"
        elif wind > 25:
            description += " &amp very windy"
        elif wind > 15:
            description += " &amp windy"
        elif wind > 5:
            description += " &amp breezy"
        else:
            description += " &amp calm"

        temp_description = "%s @ %i&deg" % (description, temp)
        return temp_description


