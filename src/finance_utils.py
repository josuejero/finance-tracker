import sqlite3
from datetime import datetime, timedelta
import os
from colorama import Fore, Style  # Add this import

DB_PATH = os.path.join(os.path.dirname(__file__), '../db/finance_tracker.db')

def calculate_balance_projection():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get current balances
        cursor.execute("SELECT amount FROM balances")
        balances = cursor.fetchall()
        total_balance = sum(balance[0] for balance in balances)
        
        # Get current payments
        cursor.execute("SELECT amount, due_date FROM payments")
        payments = cursor.fetchall()
        
        # Get current debts
        cursor.execute("SELECT min_payment, due_date FROM debts")
        debts = cursor.fetchall()
        
        # Aggregate all payments by due date
        payment_dict = {}
        for payment in payments:
            if payment[1] not in payment_dict:
                payment_dict[payment[1]] = 0
            payment_dict[payment[1]] += payment[0]
        
        for debt in debts:
            if debt[1] not in payment_dict:
                payment_dict[debt[1]] = 0
            payment_dict[debt[1]] += debt[0]
        
        # Calculate projected balance
        today = datetime.today()
        one_year_later = today + timedelta(days=365)
        current_date = today
        weekly_income = 275
        
        while current_date <= one_year_later:
            # Add weekly income on the start of the week (assuming Monday)
            if current_date.weekday() == 0:
                total_balance += weekly_income
            
            # Subtract payments due on this day
            if current_date.day in payment_dict:
                total_balance -= payment_dict[current_date.day]
            
            print(f"Balance on {current_date.strftime('%Y-%m-%d')}: {round(total_balance, 2)}")
            current_date += timedelta(days=1)
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Error calculating balance projection: {e}")

def view_balance_after_payments(up_to_date):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get the balance of the Bank of America Checking Account
        cursor.execute("SELECT amount FROM balances WHERE description = 'Bank of America Checking Account'")
        boa_balance = cursor.fetchone()
        if boa_balance:
            total_balance = boa_balance[0]
        else:
            total_balance = 0

        print(Fore.CYAN + Style.BRIGHT + f"Initial Total Balance: {total_balance}")

        # Get current payments
        cursor.execute("SELECT description, amount, due_date FROM payments")
        payments = cursor.fetchall()
        
        # Get current debts
        cursor.execute("SELECT description, min_payment, due_date FROM debts")
        debts = cursor.fetchall()
        
        # Aggregate all payments by due date
        payment_dict = {}
        for payment in payments:
            if payment[2] not in payment_dict:
                payment_dict[payment[2]] = []
            payment_dict[payment[2]].append(payment)
        
        for debt in debts:
            if debt[2] not in payment_dict:
                payment_dict[debt[2]] = []
            payment_dict[debt[2]].append(debt)
        
        # Calculate balance up to the specified date
        today = datetime.today()
        target_date = datetime.strptime(up_to_date, "%Y-%m-%d")
        current_date = today
        weekly_income = 275
        
        while current_date <= target_date:
            # Add weekly income on Sundays
            if current_date.weekday() == 6:
                total_balance += weekly_income
                print(Fore.GREEN + Style.BRIGHT + f"Payment received on {current_date.strftime('%Y-%m-%d')}: Income, Amount: {round(weekly_income, 2)}")
            
            # Subtract payments due on this day
            if current_date.day in payment_dict:
                for payment in payment_dict[current_date.day]:
                    total_balance -= payment[1]
                    print(Fore.RED + Style.BRIGHT + f"Payment due on {current_date.strftime('%Y-%m-%d')}: {payment[0]}, Amount: {round(payment[1], 2)}")
            
            print(Fore.YELLOW + Style.BRIGHT + f"Balance on {current_date.strftime('%Y-%m-%d')}: {round(total_balance, 2)}")
            current_date += timedelta(days=1)
        
        conn.close()
    except sqlite3.Error as e:
        print(Fore.RED + f"Error viewing balance after payments: {e}")

def update_balances():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM balances")
        balances = cursor.fetchall()
        for balance in balances:
            # Here you can add logic to update balances, e.g., apply interest to savings
            new_amount = balance[2]
            cursor.execute("UPDATE balances SET amount = ? WHERE id = ?", (new_amount, balance[0]))
        conn.commit()
        conn.close()
        print("Balances updated successfully")
    except sqlite3.Error as e:
        print(f"Error updating balances: {e}")

def predict_shortfalls():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Get current balances
        cursor.execute("SELECT amount FROM balances")
        balances = cursor.fetchall()
        total_balance = sum(balance[0] for balance in balances)
        
        # Get current payments
        cursor.execute("SELECT description, amount, due_date FROM payments")
        payments = cursor.fetchall()
        
        # Get current debts
        cursor.execute("SELECT description, min_payment, due_date FROM debts")
        debts = cursor.fetchall()
        
        # Calculate shortfalls
        shortfalls = []
        for payment in payments:
            if total_balance < payment[1]:
                shortfalls.append(payment)
        
        for debt in debts:
            if total_balance < debt[1]:
                shortfalls.append(debt)
        
        # Display shortfalls
        if shortfalls:
            print("Upcoming shortfalls:")
            for shortfall in shortfalls:
                print(f"{shortfall[0]}: {shortfall[1]}")
        else:
            print("No upcoming shortfalls.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Error predicting shortfalls: {e}")
