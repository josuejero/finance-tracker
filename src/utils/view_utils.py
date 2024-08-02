# src/view_utils.py

import sqlite3
import os
from colorama import Fore, Style
from tabulate import tabulate

DB_PATH = os.path.join(os.path.dirname(__file__), '../db/finance_tracker.db')

def view_table_data(table_name):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        headers = [description[0] for description in cursor.description]
        print(Fore.CYAN + Style.BRIGHT + tabulate(rows, headers=headers, tablefmt="grid"))
        conn.close()
    except sqlite3.Error as e:
        print(Fore.RED + f"Error viewing table {table_name}: {e}")

def view_balances():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM balances")
        rows = cursor.fetchall()
        headers = [description[0] for description in cursor.description]
        print(Fore.CYAN + Style.BRIGHT + tabulate(rows, headers=headers, tablefmt="grid"))
        conn.close()
    except sqlite3.Error as e:
        print(Fore.RED + f"Error viewing balances: {e}")