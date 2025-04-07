from extract_utils import get_weather_data, get_aq_data
import requests 
import logging
import os

def timestamp():
    try:
        aq_key = os.getenv("AQ_KEY")
        aq_response = requests.get(f'https://api.waqi.info/feed/London/?token={aq_key}')
        raw_aq_data = get_aq_data(aq_response)
        global timestamp 
        timestamp = list(raw_aq_data.keys())[0]

    except requests.exceptions.HTTPError as errh:
        logging.error("HTTP Error: %s", errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error("Connection Error: %s", errc)
    except requests.exceptions.Timeout as errt:
        logging.error("Timeout Error: %s", errt)
    except requests.exceptions.RequestException as err:
        logging.error("Something Else: %s", err)

    return timestamp