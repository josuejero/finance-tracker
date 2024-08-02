# src/scheduler.py

import schedule
import time
from finance_utils import update_balances

# Schedule daily updates
schedule.every().day.at("00:00").do(update_balances)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
