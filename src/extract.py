import requests
import json
from pprint import pprint

weather_response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/london?unitGroup=us&key=YPRFL9YJC993BVMCKUBCYMGFD&contentType=json')

weather_data = weather_response.json()

pprint(weather_data)