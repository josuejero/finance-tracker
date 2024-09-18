import schedule
import time
import logging
from utils.finance_utils import update_balances

def run_scheduler():
    try:
        schedule.every().day.at("00:00").do(update_balances)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        logging.error(f"Error running scheduler: {e}")
        raise

if __name__ == "__main__":
    run_scheduler()
