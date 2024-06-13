import sqlite3

def get_db_connection():
    return sqlite3.connect('database.db')

conn = get_db_connection()
cursor = conn.cursor()