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


flattened_list = []
for item in weather_data['days']:
    flattened = {}
    for key, value in item.items():
        if key == 'hours':
            continue
        else:
            flattened[key]= value
    flattened_list.append(flattened)

pprint(flattened_list)


aq_key = os.getenv("AQ_KEY")
aq_response = requests.get(f'https://api.waqi.info/feed/London/?token={aq_key}')
aq_data = aq_response.json()

# pprint(aq_data)


# import pandas as pd

# Load the JSON data into a pandas DataFrame

# df = pd.json_normalize(data, sep='_')  # Flatten nested JSON

# Write the DataFrame to a CSV file

# df.to_csv('output.csv', index=False)