# src/main.py

import schedule
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
import time
from utils.finance_utils import calculate_balance_projection, view_balance_after_payments, update_balances, predict_shortfalls
from utils.transaction_utils import add_payment, add_debt, add_balance, add_transaction, update_income_and_charges, update_balance
from utils.view_utils import view_table_data, view_balances
from init_data import initialize_data
from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)

def print_menu():
    menu_options = [
        ["1", "Add Payment"],
        ["2", "Add Debt"],
        ["3", "Add Balance"],
        ["4", "Add Transaction"],
        ["5", "Update Income and Charges"],
        ["6", "Predict Shortfalls"],
        ["7", "View Table Data"],
        ["8", "Calculate Balance Projection"],
        ["9", "View Balance After Payments"],
        ["10", "Update Existing Balance"],
        ["11", "View Balances"],
        ["12", "Exit"]
    ]
    print(Fore.CYAN + Style.BRIGHT + tabulate(menu_options, headers=["Option", "Action"], tablefmt="grid"))

def main():
    # Initialize and schedule tasks
    schedule.every().day.at("00:00").do(update_balances)

    # Add initial data
    initialize_data()

    while True:
        print(Fore.GREEN + Style.BRIGHT + "\nPlease choose an option from the menu:")
        print_menu()
        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            due_date = int(input("Enter due date (day of the month): "))
            frequency = input("Enter frequency (e.g., 'monthly'): ")
            add_payment(description, amount, due_date, frequency)
        elif choice == '2':
            description = input("Enter description: ")
            balance = float(input("Enter balance: "))
            credit_limit = float(input("Enter credit limit: "))
            due_date = int(input("Enter due date (day of the month): "))
            min_payment = float(input("Enter minimum payment: "))
            apr = float(input("Enter APR: "))
            add_debt(description, balance, credit_limit, due_date, min_payment, apr)
        elif choice == '3':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_balance(description, amount)
        elif choice == '4':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(description, amount, date)
        elif choice == '5':
            new_income = float(input("Enter new income: "))
            sudden_charges = []
            while True:
                charge_description = input("Enter charge description (or 'done' to finish): ")
                if charge_description.lower() == 'done':
                    break
                charge_amount = float(input("Enter charge amount: "))
                sudden_charges.append({'description': charge_description, 'amount': charge_amount})
            update_income_and_charges(new_income, sudden_charges)
        elif choice == '6':
            predict_shortfalls()
        elif choice == '7':
            table_name = input("Enter table name (payments, debts, balances, transactions): ")
            view_table_data(table_name)
        elif choice == '8':
            calculate_balance_projection()
        elif choice == '9':
            up_to_date = input("Enter the date up to which you want to see the balance (YYYY-MM-DD): ")
            view_balance_after_payments(up_to_date)
        elif choice == '10':
            description = input("Enter the description of the balance to update: ")
            amount = float(input("Enter the new amount: "))
            update_balance(description, amount)
        elif choice == '11':
            view_balances()
        elif choice == '12':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
        
        print(Fore.MAGENTA + "\nRunning scheduled tasks...")
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
