import psycopg2
import os
import logging
from cryptography.fernet import Fernet

def initialize_database(db_url, sql_path):
    try:
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        with open(sql_path, 'r') as f:
            cursor.execute(f.read())
        conn.commit()
    except Exception as e:
        logging.error(f"Database initialization error: {e}")
        raise
    finally:
        conn.close()

def encrypt_token(token):
    key = os.getenv('ENCRYPTION_KEY')
    cipher = Fernet(key)
    return cipher.encrypt(token.encode())

def decrypt_token(encrypted_token):
    key = os.getenv('ENCRYPTION_KEY')
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_token).decode()

def save_oauth_token(token):
    try:
        encrypted_token = encrypt_token(token['access_token'])
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_oauth_tokens (user_id, access_token) VALUES (%s, %s)", (1, encrypted_token))
        conn.commit()
    except Exception as e:
        logging.error(f"Error saving OAuth token: {e}")
        raise
    finally:
        conn.close()

def get_oauth_token():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cursor = conn.cursor()
        cursor.execute("SELECT access_token FROM user_oauth_tokens WHERE user_id = %s", (1,))
        result = cursor.fetchone()
        if result:
            return decrypt_token(result[0])
    except Exception as e:
        logging.error(f"Error retrieving OAuth token: {e}")
        raise
    finally:
        conn.close()
    return None
