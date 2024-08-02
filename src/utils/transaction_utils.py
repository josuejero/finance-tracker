# src/transaction_utils.py

import sqlite3
import os
from colorama import Fore, Style

DB_PATH = os.path.join(os.path.dirname(__file__), '../db/finance_tracker.db')

def add_payment(description, amount, due_date, frequency):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO payments (description, amount, due_date, frequency) VALUES (?, ?, ?, ?)",
                       (description, amount, due_date, frequency))
        conn.commit()
        conn.close()
        print(Fore.GREEN + Style.BRIGHT + f"Payment added: {description}, Amount: {amount}, Due Date: {due_date}, Frequency: {frequency}")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error adding payment: {e}")

def add_debt(description, balance, credit_limit, due_date, min_payment, apr):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO debts (description, balance, credit_limit, due_date, min_payment, apr) VALUES (?, ?, ?, ?, ?, ?)",
                       (description, balance, credit_limit, due_date, min_payment, apr))
        conn.commit()
        conn.close()
        print(Fore.GREEN + Style.BRIGHT + f"Debt added: {description}, Balance: {balance}, Limit: {credit_limit}, Due Date: {due_date}, Min Payment: {min_payment}, APR: {apr}")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error adding debt: {e}")

def add_balance(description, amount):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO balances (description, amount) VALUES (?, ?)",
                       (description, amount))
        conn.commit()
        conn.close()
        print(Fore.GREEN + Style.BRIGHT + f"Balance added: {description}, Amount: {amount}")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error adding balance: {e}")

def add_transaction(description, amount, date):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (description, amount, date) VALUES (?, ?, ?)",
                       (description, amount, date))
        conn.commit()
        conn.close()
        print(Fore.GREEN + Style.BRIGHT + f"Transaction added: {description}, Amount: {amount}, Date: {date}")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error adding transaction: {e}")

def update_income_and_charges(new_income, sudden_charges):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Update income (add new transaction)
        today = datetime.today().strftime('%Y-%m-%d')
        add_transaction("Income", new_income, today)
        
        # Add sudden charges (add new transactions)
        for charge in sudden_charges:
            add_transaction(charge['description'], -charge['amount'], today)
        
        conn.close()
        print(Fore.GREEN + Style.BRIGHT + f"Income and charges updated successfully: New Income: {new_income}, Charges: {sudden_charges}")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error updating income and charges: {e}")

def update_balance(description, amount):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("UPDATE balances SET amount = ? WHERE description = ?", (amount, description))
        conn.commit()
        conn.close()
        print(Fore.GREEN + Style.BRIGHT + f"Balance updated: {description}, New Amount: {amount}")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error updating balance: {e}")