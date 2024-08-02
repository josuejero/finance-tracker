import sqlite3
import os

def initialize_database(db_path, sql_path):
    # Get the absolute paths
    abs_db_path = os.path.abspath(db_path)
    abs_sql_path = os.path.abspath(sql_path)
    
    # Create the database directory if it doesn't exist
    os.makedirs(os.path.dirname(abs_db_path), exist_ok=True)
    
    # Connect to the database
    conn = sqlite3.connect(abs_db_path)
    cursor = conn.cursor()
    
    with open(abs_sql_path, 'r') as f:
        cursor.executescript(f.read())
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), '../db/finance_tracker.db')
    sql_path = os.path.join(os.path.dirname(__file__), '../sql/create_tables.sql')
    initialize_database(db_path, sql_path)
