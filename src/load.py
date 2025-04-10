import pg8000.native
from src.load_utils import connect_to_db


def load():
    con = connect_to_db()
    query = con.run('''SELECT EXISTS(SELECT 1 FROM information_schema.tables
                       WHERE table_catalog='DB_NAME' AND
                       table_schema='public' AND
                       table_name='TABLE_NAME');''')
    if query == True:
        continue
    else:
        # run sql file




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