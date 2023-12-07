import psycopg2
from psycopg2 import sql
import json
import time

json_file_path = "data.json"

data = []

db_params = {
    'host': 'host',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'pass',
    'port': 'port'
}

conn_string = "host={host} dbname={database} user={user} password={password} port={port}".format(**db_params)

try:  
    connection = psycopg2.connect(conn_string)
  
    cursor = connection.cursor()
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)   

    for item in data:
        print(item)
        query = sql.SQL("INSERT INTO public.\"table_name\" (\"param1\", \"param2\" ) VALUES (%s, %s);")
        cursor.execute(query, (item['param1'], item['param2']))
        connection.commit()
        time.sleep(0.1)              

except psycopg2.Error as e:
    print("Error connecting to the database:", e)

except psycopg2.ProgrammingError as e:
    print("Error executing SQL query:", e)

except psycopg2.ProgrammingError as e:
    print("Error executing SQL query:", e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
