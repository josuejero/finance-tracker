import os
import time
import schedule
import threading
import logging
from enum import Enum
from colorama import init, Fore, Style
from tabulate import tabulate
from utils.finance_utils import calculate_balance_projection, update_balances, predict_shortfalls
from utils.transaction_utils import add_payment, add_debt, add_balance, add_transaction, update_income_and_charges
from db_utils import initialize_database, save_oauth_token, get_oauth_token

init(autoreset=True)

MENU_OPTIONS = [
    ["1", "Add Payment"],
    ["2", "Add Debt"],
    ["3", "Add Balance"],
    ["4", "Add Transaction"],
    ["5", "Update Income and Charges"],
    ["6", "Predict Shortfalls"],
    ["7", "Calculate Balance Projection"],
    ["8", "Exit"]
]

class MenuOption(Enum):
    ADD_PAYMENT = '1'
    ADD_DEBT = '2'
    ADD_BALANCE = '3'
    ADD_TRANSACTION = '4'
    UPDATE_INCOME = '5'
    PREDICT_SHORTFALLS = '6'
    CALCULATE_BALANCE_PROJECTION = '7'
    EXIT = '8'

def print_menu():
    print(Fore.CYAN + Style.BRIGHT + tabulate(MENU_OPTIONS, headers=["Option", "Action"], tablefmt="grid"))

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

def handle_add_payment():
    description = input("Enter description: ")
    amount = get_float_input("Enter amount: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    frequency = input("Enter frequency (e.g., 'monthly'): ")
    add_payment(description, amount, due_date, frequency)

def handle_add_debt():
    description = input("Enter description: ")
    balance = get_float_input("Enter balance: ")
    credit_limit = get_float_input("Enter credit limit: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    min_payment = get_float_input("Enter minimum payment: ")
    apr = get_float_input("Enter APR: ")
    add_debt(description, balance, credit_limit, due_date, min_payment, apr)

def run_schedule_in_background():
    while True:
        schedule.run_pending()
        time.sleep(1)

menu_actions = {
    '1': handle_add_payment,
    '2': handle_add_debt,
    '3': handle_add_balance,
    '4': handle_add_transaction,
    '5': update_income_and_charges,
    '6': predict_shortfalls,
    '7': calculate_balance_projection
}

def main():
    db_url = os.getenv("DATABASE_URL")
    initialize_database(db_url, '../sql/create_tables.sql')

    schedule_thread = threading.Thread(target=run_schedule_in_background, daemon=True)
    schedule_thread.start()

    while True:
        print(Fore.GREEN + Style.BRIGHT + "\nPlease choose an option from the menu:")
        print_menu()
        choice = input(Fore.YELLOW + "Enter your choice: ")

        action = menu_actions.get(choice)
        if action:
            action()
        elif choice == MenuOption.EXIT.value:
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Error running application: {e}")
