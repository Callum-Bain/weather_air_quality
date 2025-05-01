from src.load_utils import connect_to_db
import pg8000

def load():
    try:
        conn = connect_to_db()
    except pg8000.exceptions.DatabaseError as e:
        print(e.args[0]['C'])

    # query = conn.run('''
    #                 SELECT EXISTS (
    #                 SELECT 1 FROM pg_catalog.pg_database
    #                 WHERE datname = 'weather_aqi') as database_exists;
    #                  ''')
    # print(query)
    # # if query == False:
    # #     print(query) 
    # #     # with open("sql/schema.sql", "r") as file:
    # #     #     sql_commands = file.read()

    # #     # for command in sql_commands.strip().split(';'):
    # #     #     if command.strip():
    #     #         conn.run(command)
    #     # print(query)        
    #     # conn.close()
    # else:
    #     print('Nothing')
    

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
