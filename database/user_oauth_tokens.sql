CREATE TABLE user_oauth_tokens (
    user_id INT PRIMARY KEY,
    access_token TEXT NOT NULL,
    refresh_token TEXT,
    token_expires_at TIMESTAMP
);