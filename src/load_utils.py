import pg8000.native
from dotenv import load_dotenv
import os

def connect_to_db():
    load_dotenv()
    conn = pg8000.native.Connection(
        user=os.getenv("RDS_USER"),
        password=os.getenv("RDS_PASSWORD"),
        # host=os.getenv("RDS_HOST"),
        database=os.getenv("RDS_NAME")
        )
    return conn