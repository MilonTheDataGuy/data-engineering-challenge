import sqlite3
import random
from datetime import datetime, timedelta
import os

def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    cursor.executescript(sql_script)

def create_ratings_table(cursor):
    # creating ratings table
    execute_sql_file(cursor, 'src/sql/create_ratings_table.sql')

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = (end_date - start_date).days

    for _ in range(100000):
        timestamp = start_date + timedelta(days=random.randint(0, date_range))
        user_id = random.randint(1, 1000)
        product_id = random.randint(1, 1000)
        rating = random.randint(1, 5)
        cursor.execute('''
        INSERT INTO Ratings (timestamp, user_id, product_id, rating)
        VALUES (?, ?, ?, ?)
        ''', (timestamp, user_id, product_id, rating))
  
if __name__ == '__main__':
    # Ensure the data directory exists if not will create it
    os.makedirs('data', exist_ok=True)

    # create a sqlite db connection
    conn = sqlite3.connect('data/ratings.db')
    cursor = conn.cursor()

    create_ratings_table(cursor)
    conn.commit()

    execute_sql_file(cursor, 'src/sql/create_aggregates_table.sql')
    conn.commit()
    
    # closing sqlite connection 
    conn.close()