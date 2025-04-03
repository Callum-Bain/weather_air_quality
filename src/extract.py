from extract_utils import get_weather_data, get_aq_data
import requests
import json
import os
import pandas as pd
from pprint import pprint
from dotenv import load_dotenv


weather_key = os.getenv("WEATHER_KEY")
weather_response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/london?unitGroup=us&key={weather_key}&contentType=json')
raw_weather_data = get_weather_data(weather_response)

aq_key = os.getenv("AQ_KEY")
aq_response = requests.get(f'https://api.waqi.info/feed/London/?token={aq_key}')
raw_aq_data = get_aq_data(aq_response)
timestamp = list(raw_aq_data.keys())[0]

with open(f'data/weather_output_{timestamp}.txt', 'w') as file:
    file.write(str(raw_weather_data))

with open(f'data/aq_output_{timestamp}.txt', 'w') as file:
    file.write(str(raw_aq_data))

