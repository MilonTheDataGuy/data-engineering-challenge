import sqlite3
  
def execute_fetch_query(cursor, file_path):
    with open(file_path, 'r') as file:
        query = file.read()
    cursor.execute(query)
    top_products = cursor.fetchall()
    return top_products
  
if __name__ == '__main__':
    conn = sqlite3.connect('data/ratings.db')
    cursor = conn.cursor()

    # Find the top-rated products for each month
    top_products = execute_fetch_query(cursor, 'src/sql/top_products.sql')
    for product in top_products:
        print(product)
  
    # Closing the connection
    conn.close()
