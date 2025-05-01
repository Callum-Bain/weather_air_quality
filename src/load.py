from src.load_utils import connect_to_db

def load():
    
    conn = connect_to_db()
    query = conn.run('''SELECT EXISTS(SELECT 1 FROM information_schema.tables
                       WHERE table_catalog='weather_api' AND
                       table_schema='public');''')
    if query == False:
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