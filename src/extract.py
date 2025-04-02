import requests
import json
from pprint import pprint

response = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/london?unitGroup=us&key=YPRFL9YJC993BVMCKUBCYMGFD&contentType=json')

data = response.json()

pprint(data)