import sqlite3
from database.connection import get_db_connection

def create_table():
        
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL UNIQUE,
        age TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        Food_id INTEGER,
        FOREIGN KEY (Food_id) REFERENCES Food(id)
    )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Nutritionist (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          phone_number TEXT NOT NULL UNIQUE,
          email TEXT NOT NULL,
          consultation_fee REAL NOT NULL,
          password TEXT NOT NULL
        )
    """)
            
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Food (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          category TEXT NOT NULL,
          calories REAL NOT NULL,
          descriptions TEXT NOT NULL,
          Nutri_id INTEGER,
          FOREIGN KEY (Nutri_id) REFERENCES Nutritionist(id)
        )
    """)

    

    conn.commit()
    conn.close()
