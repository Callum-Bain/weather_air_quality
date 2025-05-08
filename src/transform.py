from src.transform_utils import aqi_categories
import json
import pandas as pd
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

def transform():
    """""
    1. Convert the JSON file into a Python Object
    2. Convert Python Object into a tabular data structure
    3. Save the output as a file
    """""

    with open('timestamp.csv','r') as timestamp_file:
        lines = timestamp_file.readlines()
        last_line = lines[-1].strip() if lines else ""
        current_date = last_line[0:10]
        current_time = last_line[11:]

    with open(f'data/Extract/weather_output_{last_line}.json', 'r') as weather_file:
        weather_load = json.load(weather_file)
        weather_data_list = weather_load[f'{current_date}']

        weather_df = pd.DataFrame(weather_data_list)
        weather_df['date'] = current_date
        weather_df['datetime_stamp'] = last_line
        weather_df['temp'] = round((weather_df['temp'] - 32) / 1.8, 2)
        weather_df['feelslike'] = round((weather_df['feelslike'] - 32) / 1.8, 2)
        new_weather_df = weather_df.drop(columns=['stations', 'datetimeEpoch'], inplace=False)
        new_weather_df = new_weather_df[
                    ['datetime_stamp',
                        'date',
                        'datetime',
                        'temp',
                        'feelslike',
                        'humidity',
                        'dew',
                        'precip',
                        'precipprob',
                        'snow',
                        'snowdepth',
                        'preciptype',
                        'windgust',
                        'windspeed',
                        'winddir',
                        'pressure',
                        'visibility',
                        'cloudcover',
                        'solarradiation',
                        'solarenergy',
                        'uvindex',
                        'severerisk',
                        'conditions',
                        'icon',
                        'source']]

    with open(f'data/Extract/aq_output_{last_line}.json', 'r') as aq_file:
        aq_load = json.load(aq_file)
        aq_data_dict = aq_load[last_line]
        aqi_data = aq_load['aqi']
        aq_df = pd.DataFrame(aq_data_dict)
        aq_df['date'] = current_date
        aq_df['datetime'] = current_time
        aq_df['datetime_stamp'] = last_line
        aq_df['AQI'] = aqi_data
        aq_df['AQI Category'] = aq_df['AQI'].apply(aqi_categories)
        new_aq_df = aq_df.reset_index(drop=True)
        new_aq_df = new_aq_df[
                ['datetime_stamp',
                    'co',
                    'h',
                    'no2',
                    'o3',
                    'p',
                    'pm10',
                    'pm25',
                    'so2',
                    't',
                    'w',
                    'date',
                    'datetime',
                    'AQI',
                    'AQI Category']]

    # Final Weather Dataframe
    weather_hour_df = new_weather_df[new_weather_df['datetime'].isin(aq_df['datetime'])]

    if os.path.exists('data/Transform/weather_transformed_data.csv'):
        with open('data/Transform/weather_transformed_data.csv','r') as weather_timestamp_file:
            lines = weather_timestamp_file.readlines()
            weather_timestamp = lines[-1][:19]

    # Create CSV weather output file
    if not os.path.exists('data/Transform/weather_transformed_data.csv'):
        weather_hour_df.to_csv('data/Transform/weather_transformed_data.csv', index=False)
    elif (weather_hour_df['datetime_stamp'] != weather_timestamp).any():
        weather_hour_df.to_csv('data/Transform/weather_transformed_data.csv', index=False, mode='a', header=False)
    else:
        logging.warning("Unable to append weather data (data for this hour has already been recorded)")

    # Create CSV AQ output file
    if not os.path.exists('data/Transform/air_quality_transformed_data.csv'):
        new_aq_df.to_csv('data/Transform/air_quality_transformed_data.csv', index=False)
    elif (new_aq_df['datetime_stamp'] != weather_timestamp).any():
        new_aq_df.to_csv('data/Transform/air_quality_transformed_data.csv', index=False, mode='a', header=False)
    else:
        logging.warning("Unable to append air quality data (data for this hour has already been recorded)")


transform()