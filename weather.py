#!/Users/andrew.cathcart/.local/share/virtualenvs/rainy-or-not-kja58eca/bin/python

import os
import requests
import json
import sys
from datetime import datetime

API_KEY = os.environ["OPENWEATHERMAP_API_KEY"]

payload = {
    "APPID": API_KEY,
    "q": "newcastle,gb"
}
URL = "http://api.openweathermap.org/data/2.5/weather"

if len(sys.argv) > 1 and sys.argv[1] == 'forecast':
    URL = "http://api.openweathermap.org/data/2.5/forecast"
    r = requests.get(URL, params=payload).json()

    current_date = datetime.now().date()
    for el in r["list"]:
        forecast_datetime = datetime.utcfromtimestamp(el["dt"])
        forecast_date = datetime.date(forecast_datetime)

        # exit the loop after we've printed forecast information for today
        if forecast_date != current_date:
            break

        weather_description = el["weather"][0]["description"]
        print(forecast_datetime, weather_description)
else:
    r = requests.get(URL, params=payload).json()
    print("Weather currently:", r["weather"][0]["description"])
