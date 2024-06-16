import sqlite3
from database.connection import get_db_connection

class User:
    def __init__(self, id, name, phone_number, age, username, password, food_id=None):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.username = username
        self.password = password
        self.food_id = food_id

    def save(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO User (name, phone_number, age, username, password, Food_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.name, self.phone_number, self.age, self.username, self.password, self.food_id))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_username(cls, username):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM User WHERE username=?", (username,))
        user_data = cur.fetchone()
        conn.close()
        if user_data:
            return cls(*user_data)  # Unpacks the tuple to instantiate the User object
        else:
            return None

    @classmethod
    def authenticate(cls, username, password):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM User WHERE username=?", (username,))
        user_data = cur.fetchone()
        conn.close()
        
        if user_data and user_data[5] == password:  # user_data[5] is the password field index in the database
            return cls(*user_data)  # Unpacks the tuple to instantiate the User object
        else:
            return None

    # Add other methods as needed


    # Add other methods as needed






#    