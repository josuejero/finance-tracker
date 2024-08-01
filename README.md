# Finance Tracker

Finance Tracker is a Python-based application designed to help users manage their personal finances by tracking payments, debts, balances, and transactions. The application uses SQLite for data storage and provides a command-line interface for interaction.

## Project Structure

```

├── all_code.txt
├── db
│   └── finance_tracker.db
├── problem.py
├── sql
│   └── create_tables.sql
└── src
    ├── __pycache__
    ├── db_utils.py
    ├── finance_utils.py
    ├── init_data.py
    ├── main.py
    ├── scheduler.py
    ├── transaction_utils.py
    ├── verify_db.py
    └── view_utils.py
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone [<repository-url>](https://github.com/josuejero/finance-tracker)
   cd finance-tracker
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Make sure you have the required packages installed. You can use pip to install them:

   ```bash
   pip install -r requirements.txt
   ```

   *(Note: Create a `requirements.txt` file listing your project's dependencies, e.g., `colorama`, `tabulate`, `schedule`.)*

4. **Initialize the Database**

   Run the following command to set up the database:

   ```bash
   python src/db_utils.py
   ```

5. **Run the Application**

   ```bash
   python src/main.py
   ```

## Usage

Once the application is running, you can perform various financial management tasks such as:

- Adding payments, debts, balances, and transactions.
- Viewing current balances and transactions.
- Predicting shortfalls.
- Calculating balance projections.

### Main Menu Options

- **Add Payment**: Record a new payment.
- **Add Debt**: Record a new debt.
- **Add Balance**: Add an account balance.
- **Add Transaction**: Add a new financial transaction.
- **Update Income and Charges**: Update income and unexpected charges.
- **Predict Shortfalls**: Analyze and predict financial shortfalls.
- **View Table Data**: View data from specific tables.
- **Calculate Balance Projection**: Project future balances based on current data.
- **View Balance After Payments**: See projected balances after payments.
- **Update Existing Balance**: Update the balance of an existing account.
- **View Balances**: View current account balances.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create a pull request or submit an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Colorama](https://pypi.org/project/colorama/)
- [Tabulate](https://pypi.org/project/tabulate/)
- [Schedule](https://pypi.org/project/schedule/)
