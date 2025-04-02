import requests
import json
from pprint import pprint

weather_response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/london?unitGroup=us&key=YPRFL9YJC993BVMCKUBCYMGFD&contentType=json')

weather_data = weather_response.json()

aq_response = requests.get('https://api.waqi.info/feed/London/?token=ba82ebbfeadd9c7b6cf12f43bc150dd3039ac2e2')

aq_data = aq_response.json()

pprint(aq_data)