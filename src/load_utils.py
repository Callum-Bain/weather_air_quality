from pg8000.native import Connection
import dotenv
import os

dotenv.load_dotenv(override=True)

def connect_to_db():

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
