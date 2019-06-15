import os
import requests
import json

API_KEY = os.environ["OPENWEATHERMAP_API_KEY"]
URL = "http://api.openweathermap.org/data/2.5/weather"
payload = {
    "APPID": API_KEY,
    "q": "newcastle,gb"
}

r = requests.get(URL, params=payload).json()
print("Weather currently:", r["weather"][0]["description"])
