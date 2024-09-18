import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "../db/finance_tracker.db")

def check_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        if tables:
            print("Tables found in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")

if __name__ == "__main__":
    check_tables()
