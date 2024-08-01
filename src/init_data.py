# src/init_data.py

from transaction_utils import add_payment, add_debt, add_balance
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../db/finance_tracker.db')

def delete_records_and_reset_autoincrement(table):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table}")
    cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}'")
    conn.commit()
    conn.close()

def initialize_data():
    print("Let's set up your financial data.")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Clear existing data
    for table in ['payments', 'debts', 'balances']:
        delete_records_and_reset_autoincrement(table)

    # Add Payments
    payments = []
    print("Enter your payment details. Type 'done' to finish.")
    while True:
        description = input("Payment Description (or 'done' to stop): ")
        if description.lower() == 'done':
            break
        amount = float(input("Amount: "))
        due_date = int(input("Due date (day of month): "))
        frequency = input("Frequency (e.g., 'monthly'): ")
        payments.append((description, amount, due_date, frequency))

    for payment in payments:
        add_payment(*payment)

    # Add Debts
    debts = []
    print("Enter your debt details. Type 'done' to finish.")
    while True:
        description = input("Debt Description (or 'done' to stop): ")
        if description.lower() == 'done':
            break
        balance = float(input("Balance: "))
        credit_limit = float(input("Credit limit: "))
        due_date = int(input("Due date (day of month): "))
        min_payment = float(input("Minimum payment: "))
        apr = float(input("APR: "))
        debts.append((description, balance, credit_limit, due_date, min_payment, apr))

    for debt in debts:
        add_debt(*debt)

    # Add Balances
    balances = []
    print("Enter your balance details. Type 'done' to finish.")
    while True:
        description = input("Account Description (or 'done' to stop): ")
        if description.lower() == 'done':
            break
        amount = float(input("Amount: "))
        balances.append((description, amount))

    for balance in balances:
        add_balance(*balance)

    conn.close()

if __name__ == "__main__":
    initialize_data()
