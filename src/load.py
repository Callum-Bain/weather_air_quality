from src.load_utils import create_database, connect_to_weather_db

def load():
    create_database()
    conn = connect_to_weather_db()
    # conn.run a query for insert into or insert using pandas
    # 


load()
# Load in transformed data
# SQL schema
# conditional logic to see if database already exists
#  - if not then create database else continue
# enter data into sql schema
# load SQL schema into database

'''
Query to check if a databse exists:
SELECT EXISTS(SELECT 1 FROM information_schema.tables
              WHERE table_catalog='DB_NAME' AND
                    table_schema='public' AND
                    table_name='TABLE_NAME');
'''
