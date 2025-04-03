import requests
import json
import os
import pandas as pd
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

weather_key = os.getenv("WEATHER_KEY")
weather_response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/london?unitGroup=us&key={weather_key}&contentType=json')
weather_data = weather_response.json()

flat_weather_date = weather_data['days'][0]['datetime']
flat_weather = weather_data['days'][0]['hours']
combined_weather = {flat_weather_date: flat_weather}


aq_key = os.getenv("AQ_KEY")
aq_response = requests.get(f'https://api.waqi.info/feed/London/?token={aq_key}')
aq_data = aq_response.json()

flat_aq_date = aq_data['data']['time']['s']
flat_aq_data = aq_data['data']['iaqi']
combined_aq = {flat_aq_date: flat_aq_data}
pprint(combined_aq)
