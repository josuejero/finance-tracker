import sqlite3
import os
import logging

DB_PATH = os.getenv("DB_PATH", "../db/finance_tracker.db")

def add_payment(description, amount, due_date, frequency):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")
            cursor.execute("INSERT INTO payments (description, amount, due_date, frequency) VALUES (?, ?, ?, ?)",
                           (description, amount, due_date, frequency))
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        logging.error(f"Error adding payment: {e}")
        raise
    finally:
        conn.close()

def add_debt(description, balance, credit_limit, due_date, min_payment, apr):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")
            cursor.execute("INSERT INTO debts (description, balance, credit_limit, due_date, min_payment, apr) VALUES (?, ?, ?, ?, ?, ?)",
                           (description, balance, credit_limit, due_date, min_payment, apr))
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        logging.error(f"Error adding debt: {e}")
        raise
    finally:
        conn.close()

def add_balance(description, amount):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")
            cursor.execute("INSERT INTO balances (description, amount) VALUES (?, ?)", (description, amount))
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        logging.error(f"Error adding balance: {e}")
        raise
    finally:
        conn.close()

def add_transaction(description, amount, date):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            conn.execute("BEGIN")
            cursor.execute("INSERT INTO transactions (description, amount, date) VALUES (?, ?, ?)",
                           (description, amount, date))
            conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        logging.error(f"Error adding transaction: {e}")
        raise
    finally:
        conn.close()
