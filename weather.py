#!/Users/andrew.cathcart/.local/share/virtualenvs/rainy-or-not-kja58eca/bin/python

import os
import requests
import json
import sys
from datetime import datetime
import pandas as pd


def kelvin_to_celsius(kelvin):
    """ Openweather returns temperature readings in Kelvin, need to convert this"""
    return round(kelvin - 273.15, 2)


def print_weather_summary():
    URL = "http://api.openweathermap.org/data/2.5/weather"
    r = requests.get(URL, params=payload).json()
    dt = datetime.utcfromtimestamp(r["dt"] + r["timezone"])

    description, temp, temp_min, temp_max = description_and_temperature(r)

    df = pd.DataFrame({"Description": description, "Temp (°C)": temp, "Min (°C)": temp_min,
                       "Max (°C)": temp_max}, index=[dt])

    print(df)


def print_forecast_summary():
    URL = "http://api.openweathermap.org/data/2.5/forecast"
    r = requests.get(URL, params=payload).json()

    current_date = datetime.now().date()
    forecast_list = []
    for el in r["list"]:
        forecast_datetime = datetime.utcfromtimestamp(
            el["dt"])

        # exit the loop after we've printed forecast information for today
        if forecast_datetime.date() != current_date:
            break

        description, temp, temp_min, temp_max = description_and_temperature(el)

        df = pd.DataFrame({"Description": description, "Temp (°C)": temp, "Min (°C)": temp_min,
                           "Max (°C)": temp_max}, index=[forecast_datetime])
        forecast_list.append(df)

    df = pd.concat(forecast_list)
    print(df)


def description_and_temperature(obj):
    main = obj["main"]
    description = obj["weather"][0]["description"]
    temp = kelvin_to_celsius(main["temp"])
    temp_min = kelvin_to_celsius(main["temp_min"])
    temp_max = kelvin_to_celsius(main["temp_max"])
    return description, temp, temp_min, temp_max


API_KEY = os.environ["OPENWEATHERMAP_API_KEY"]

payload = {
    "APPID": API_KEY,
    "q": "newcastle upon tyne,gb"
}

if len(sys.argv) > 1 and sys.argv[1] == 'forecast':
    print_forecast_summary()
else:
    print_weather_summary()
