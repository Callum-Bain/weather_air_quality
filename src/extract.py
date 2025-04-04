from extract_utils import get_weather_data, get_aq_data
import requests
import json
import os
import pandas as pd
from pprint import pprint
from dotenv import load_dotenv
import logging

load_dotenv() 

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

try:
    weather_key = os.getenv("WEATHER_KEY")
    weather_response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/london?unitGroup=us&key={weather_key}&contentType=json')
    raw_weather_data = get_weather_data(weather_response)
except requests.exceptions.HTTPError as errh:
    logging.error("HTTP Error: %s", errh)
except requests.exceptions.ConnectionError as errc:
    logging.error("Connection Error: %s", errc)
except requests.exceptions.Timeout as errt:
    logging.error("Timeout Error: %s", errt)
except requests.exceptions.RequestException as err:
    logging.error("Something Else: %s", err)

try:
    aq_key = os.getenv("AQ_KEY")
    aq_response = requests.get(f'https://api.waqi.info/feed/London/?token={aq_key}')
    raw_aq_data = get_aq_data(aq_response)
    timestamp = list(raw_aq_data.keys())[0]
except requests.exceptions.HTTPError as errh:
    logging.error("HTTP Error: %s", errh)
except requests.exceptions.ConnectionError as errc:
    logging.error("Connection Error: %s", errc)
except requests.exceptions.Timeout as errt:
    logging.error("Timeout Error: %s", errt)
except requests.exceptions.RequestException as err:
    logging.error("Something Else: %s", err)

with open(f'data/weather_output_{timestamp}.json', 'w') as file:
    json.dump(raw_weather_data, file)

with open(f'data/aq_output_{timestamp}.json', 'w') as file:
    json.dump(raw_aq_data, file)

