-- sql/create_tables.sql

-- payments table
CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    due_date INTEGER NOT NULL,
    frequency TEXT NOT NULL
);

-- debts table
CREATE TABLE debts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    balance REAL NOT NULL,
    credit_limit REAL NOT NULL,
    due_date INTEGER NOT NULL,
    min_payment REAL NOT NULL,
    apr REAL NOT NULL
);

-- balances table
CREATE TABLE balances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL
);

-- transactions table
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
);
