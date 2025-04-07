import json
import pandas as pd

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

        with open(f'data/weather_output_{last_line}.json', 'r') as weather_file:
            weather_load = json.load(weather_file)
            weather_data_list = weather_load[f'{current_date}']

            weather_df = pd.DataFrame(weather_data_list)
            weather_df['date'] = current_date
            weather_df['temp'] = round((weather_df['temp'] - 32) / 1.8, 2)
            weather_df['feelslike'] = round((weather_df['feelslike'] - 32) / 1.8, 2)
            new_weather_df = weather_df.drop(columns=['stations'], inplace=False)
            print(new_weather_df)    
           
        with open(f'data/aq_output_{last_line}.json', 'r') as aq_file:
            aq_load = json.load(aq_file)
            aq_data_dict = aq_load[last_line]
            aq_df = pd.DataFrame(aq_data_dict)
            aq_df['date'] = current_date
            new = aq_df.reset_index(drop=True)
     
            # print(new)

transform()