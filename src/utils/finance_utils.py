import sqlite3
from datetime import datetime, timedelta
import os
import logging

DB_PATH = os.getenv("DB_PATH", "../db/finance_tracker.db")

def calculate_balance_projection():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT amount FROM balances")
            balances = cursor.fetchall()
            total_balance = sum(balance[0] for balance in balances)
            
            cursor.execute("SELECT amount, due_date FROM payments")
            payments = cursor.fetchall()
            
            cursor.execute("SELECT min_payment, due_date FROM debts")
            debts = cursor.fetchall()
            
            payment_dict = {}
            for payment in payments:
                if payment[1] not in payment_dict:
                    payment_dict[payment[1]] = 0
                payment_dict[payment[1]] += payment[0]

            for debt in debts:
                if debt[1] not in payment_dict:
                    payment_dict[debt[1]] = 0
                payment_dict[debt[1]] += debt[0]
            
            today = datetime.today()
            one_year_later = today + timedelta(days=365)
            current_date = today
            weekly_income = 275

            while current_date <= one_year_later:
                if current_date.weekday() == 0:
                    total_balance += weekly_income

                if current_date in payment_dict:
                    total_balance -= payment_dict[current_date]
                
                print(f"Balance on {current_date.strftime('%Y-%m-%d')}: {round(total_balance, 2)}")
                current_date += timedelta(days=1)
    except sqlite3.Error as e:
        logging.error(f"Error calculating balance projection: {e}")
        raise

def predict_shortfalls():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT amount FROM balances")
            balances = cursor.fetchall()
            total_balance = sum(balance[0] for balance in balances)

            cursor.execute("SELECT description, amount, due_date FROM payments")
            payments = cursor.fetchall()

            cursor.execute("SELECT description, min_payment, due_date FROM debts")
            debts = cursor.fetchall()

            shortfalls = []
            for payment in payments:
                if total_balance < payment[1]:
                    shortfalls.append(payment)
            
            for debt in debts:
                if total_balance < debt[1]:
                    shortfalls.append(debt)

            if shortfalls:
                print("Upcoming shortfalls:")
                for shortfall in shortfalls:
                    print(f"{shortfall[0]}: {shortfall[1]}")
            else:
                print("No upcoming shortfalls.")
    except sqlite3.Error as e:
        logging.error(f"Error predicting shortfalls: {e}")
        raise
