import psycopg2
import pandas as pd
import csv
import os
from dotenv import load_dotenv
from utils import get_table_names, get_count_table

load_dotenv()
global connection1, connection2

# Connect to both databases
try:
    connection1 = psycopg2.connect(
        host=os.environ.get('HOST', 'localhost'),
        database=os.environ.get('DATABASE_ONE', 'upp'),
        user=os.environ.get('USER_DB', ''),
        password=os.environ.get('PASSWORD_DB', '')
    )
except psycopg2.OperationalError as e:
    print(f"Got this error: {e}")
    
try:
    connection2 = psycopg2.connect(
        host=os.environ.get('HOST', 'localhost'),
        database=os.environ.get('DATABASE_TWO', 'erd'),
        user=os.environ.get('USER_DB', ''),
        password=os.environ.get('PASSWORD_DB', '')
    )
except psycopg2.OperationalError as e:
    print(f"Got this error: {e}")

# Get all table names in db1
table_names = get_table_names(connection1)

# Prepare csv for logging
with open('log.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Table', 'DB1 Count', 'DB2 Count', 'Match'])

    # For each table, check the count in both DBs and log the result
    for table_name in table_names:
        count1 = get_count_table(connection1, table_name)
        count2 = get_count_table(connection2, table_name)
        
        writer.writerow([table_name, count1, count2, count1 == count2])

connection1.close()
connection2.close()
