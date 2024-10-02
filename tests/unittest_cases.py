import unittest  
import sqlite3  
import os  
import sys  
  
# Add the src directory to the Python path  
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))  
  
from main import create_ratings_table, execute_sql_file  
from execute_sql import execute_fetch_query  
  
def setUpModule():  
    # Ensure the data directory exists  
    os.makedirs(os.path.abspath('../data'), exist_ok=True)  
  
    # Create a sqlite db connection  
    global conn  
    global cursor  
    conn = sqlite3.connect(os.path.abspath('../data/test_ratings.db'))  
    cursor = conn.cursor()  
  
    # Create and populate the Ratings table  
    create_ratings_table(cursor)  
  
    # Execute additional SQL file to create RatingsMonthlyAggregates table  
    execute_sql_file(cursor, 'src/sql/create_aggregates_table.sql')  
  
def tearDownModule():  
    # Close the sqlite connection  
    conn.close()  
    # Clean up the test database file  
    os.remove(os.path.abspath('../data/test_ratings.db'))  
  
class TestDatabase(unittest.TestCase):  
  
    def test_ratings_table_creation(self):  
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Ratings';")  
        self.assertIsNotNone(cursor.fetchone(), "Ratings table should be created")  
  
    def test_ratings_table_population(self):  
        cursor.execute("SELECT COUNT(*) FROM Ratings;")  
        count = cursor.fetchone()[0]  
        self.assertEqual(count, 100000, "Ratings table should be populated with 1,00,000 rows")  
  
    def test_aggregates_table_creation(self):  
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='RatingsMonthlyAggregates';")  
        self.assertIsNotNone(cursor.fetchone(), "RatingsMonthlyAggregates table should be created")  
  
    def test_monthly_top_rated_products(self):  
        # Use the execute_fetch_query function to get the top-rated products  
        top_products = execute_fetch_query(cursor, 'src/sql/top_products.sql')  
  
        # Check that there are results for each month of 2024  
        months = set()  
        for product in top_products:
            month = product[0]
            months.add(month)
            self.assertGreaterEqual(product[1], 3, f"Month {month} should have at least 3 top-rated products")  
        self.assertEqual(len(months), 12, "There should be results for each month of 2024")  

if __name__ == '__main__':
    unittest.main()