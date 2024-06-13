from models.Food import Food
from models.User import User
import sqlite3

def get_db_connection():
    return sqlite3.connect('database.db')

class Nutritionist:
    TABLE_NAME = "Nutritionist"

    def __init__(self, id, name, phone_number, email):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name, phone_number, email)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.phone_number, self.email))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"{self.name} saved")

    def dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email
        }

    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            DROP TABLE IF EXISTS {cls.TABLE_NAME}
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def find(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
        """
        rows = cursor.execute(sql).fetchall()
        return [
            cls.row_to_instance(row).dictionary() for row in rows
        ]

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        nutritionist = cls(None, row[1], row[2], row[3])
        nutritionist.id = row[0]
        return nutritionist