from src.load_utils import connect_to_weather_db, connect_to_postgres_db
import pg8000

def load():
    try:
        conn = connect_to_weather_db()
    except pg8000.exceptions.DatabaseError as e:
        if e.args[0]['C'] == '3D000':
            conn = connect_to_postgres_db()
            query = 'CREATE DATABASE weather_aqi;'
            conn.run(query)
            conn.close()
            conn = connect_to_weather_db()

            with open("sql/schema.sql", "r") as file:
                sql_commands = file.read()

            for command in sql_commands.strip().split(';'):
                if command.strip():
                    conn.run(command)
            conn.close()


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
