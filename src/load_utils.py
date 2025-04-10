import pg8000.native
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_db():
    con = pg8000.native.Connection(
        user=os.getenv("RDS_USER"),
        password=os.getenv("RDS_PASSWORD"),
        host=os.getenv("RDS_HOST"),
        database=os.getenv("RDS_NAME"))
    return con