from datetime import datetime, timedelta

def get_weather_data(weather_response):
    weather_data = weather_response.json()
    flat_weather_date = weather_data['days'][0]['datetime']
    flat_weather = weather_data['days'][0]['hours']
    return {flat_weather_date: flat_weather}


def get_aq_data(aq_response):
    aq_data = aq_response.json()
    flat_aq_date = aq_data['data']['time']['s']
    formatted_timestamp = datetime.strptime(flat_aq_date, "%Y-%m-%d %H:%M:%S") + timedelta(hours=2)
    formatted_timestamp = str(formatted_timestamp)
    flat_aq_data = aq_data['data']['iaqi']
    return {formatted_timestamp: flat_aq_data}