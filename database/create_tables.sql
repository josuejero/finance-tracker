
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS debts;
DROP TABLE IF EXISTS balances;
DROP TABLE IF EXISTS user_oauth_tokens;

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount >= 0),
    due_date DATE NOT NULL,
    frequency TEXT NOT NULL CHECK (frequency IN ('weekly', 'monthly', 'yearly'))
);

CREATE TABLE debts (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    balance NUMERIC(10, 2) NOT NULL CHECK (balance >= 0),
    credit_limit NUMERIC(10, 2) NOT NULL CHECK (credit_limit >= 0),
    due_date DATE NOT NULL,
    min_payment NUMERIC(10, 2) NOT NULL CHECK (min_payment >= 0),
    apr NUMERIC(5, 2) NOT NULL CHECK (apr >= 0)
);

CREATE TABLE balances (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount >= 0)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    date DATE NOT NULL,
    payment_id INTEGER REFERENCES payments(id) ON DELETE CASCADE
);

CREATE TABLE user_oauth_tokens (
    user_id INT PRIMARY KEY,
    access_token TEXT NOT NULL,
    refresh_token TEXT,
    token_expires_at TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_transactions_description ON transactions(description);

CREATE INDEX IF NOT EXISTS idx_payments_due_date ON payments(due_date);
CREATE INDEX IF NOT EXISTS idx_debts_due_date ON debts(due_date);
CREATE INDEX IF NOT EXISTS idx_transactions_date ON transactions(date);
