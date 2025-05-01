from pg8000.native import Connection
import pg8000
import dotenv
import os

dotenv.load_dotenv(override=True)

def connect_to_weather_db():

    user = os.environ["RDS_USER"]
    password = os.environ["RDS_PASSWORD"]
    host = os.environ["RDS_HOST"]
    port = os.environ["RDS_PORT"]
    database = os.environ["RDS_NAME"]

    return Connection(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
        )


def connect_to_postgres_db():

    user = os.environ["RDS_USER"]
    password = os.environ["RDS_PASSWORD"]
    host = os.environ["RDS_HOST"]
    port = os.environ["RDS_PORT"]
    database = os.environ["RDS_LOCAL_NAME"]

    return Connection(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
        )


def create_database():
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
    finally:
        conn.close()
