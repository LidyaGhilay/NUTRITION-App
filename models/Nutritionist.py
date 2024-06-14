import sqlite3
from database.connection import get_db_connection

class Nutritionist:
    
    TABLE_NAME = "Nutritionist"

    def __init__(self, id, name, phone_number, email, consultation_fee, password):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.consultation_fee = consultation_fee
        self.password = password

    @staticmethod
    def add_nutritionist(name, phone_number, email, consultation_fee, password):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Nutritionist (name, phone_number, email, consultation_fee, password) VALUES (?, ?, ?, ?, ?)", 
                    (name, phone_number, email, consultation_fee, password))
        conn.commit()
        conn.close()  # Don't forget to close the connection

    @staticmethod
    def authenticate(email, password):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Nutritionist WHERE email = ? AND password = ?", (email, password))
        nutritionist = cur.fetchone()
        conn.close()
        if nutritionist:
            return Nutritionist(*nutritionist)
        else:
            return None

   
   
   
    # def save(self):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     sql = f"""
    #         INSERT INTO {self.TABLE_NAME} (name, phone_number, email, consultation_fee)
    #         VALUES (?, ?, ?, ?)
    #     """
    #     cursor.execute(sql, (self.name, self.phone_number, self.email, self.consultation_fee))
    #     conn.commit()
    #     self.id = cursor.lastrowid
    #     print(f"{self.name} saved")

   
        

    # def dictionary(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "phone_number": self.phone_number,
    #         "email": self.email,
    #         "consultation_fee": self.consultation_fee
    #     }

    # @classmethod
    # def drop_table(cls):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     sql = f"""
    #         DROP TABLE IF EXISTS {cls.TABLE_NAME}
    #     """
    #     cursor.execute(sql)
    #     conn.commit()

    # def update(self):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     sql = f"""
    #         UPDATE {self.TABLE_NAME} SET name=?, phone_number=?, email=?, consultation_fee=? WHERE id=?
    #     """
    #     cursor.execute(sql, (self.name, self.phone_number, self.email, self.consultation_fee, self.id))
    #     conn.commit()
    #     print(f"{self.name} updated")

    # def delete(self):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     sql = f"""
    #         DELETE FROM {self.TABLE_NAME} WHERE id = ?
    #     """
    #     cursor.execute(sql, (self.id,))
    #     conn.commit()
    #     print(f"{self.name} deleted")

    # @classmethod
    # def find(cls):
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     sql = f"""
    #         SELECT * FROM {cls.TABLE_NAME}
    #     """
    #     rows = cursor.execute(sql).fetchall()
    #     return [
    #         cls.row_to_instance(row).dictionary() for row in rows
    #     ]

    # @classmethod
    # def row_to_instance(cls, row):
    #     if row is None:
    #         return None
    #     nutritionist = cls(None, row[1], row[2], row[3], row[4])
    #     nutritionist.id = row[0]
    #     return nutritionist
