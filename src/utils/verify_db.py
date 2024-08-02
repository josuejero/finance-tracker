# src/verify_db.py

import sqlite3
import os
from colorama import Fore, Style
from tabulate import tabulate

DB_PATH = os.path.join(os.path.dirname(__file__), '../db/finance_tracker.db')

def view_table_structure(table_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    rows = cursor.fetchall()
    headers = ["cid", "name", "type", "notnull", "dflt_value", "pk"]
    print(Fore.CYAN + Style.BRIGHT + tabulate(rows, headers=headers, tablefmt="grid"))
    conn.close()

if __name__ == "__main__":
    table_name = input("Enter table name to view its structure: ")
    view_table_structure(table_name)
