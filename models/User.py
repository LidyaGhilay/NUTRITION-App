import sqlite3
from database.connection import get_db_connection

class User:
    
    TABLE_NAME = "userDetails"

    def __init__(self, id, name, phone_number, age, username, password, Food_id):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.username = username
        self.password = password
        self.Food_id = Food_id

    @staticmethod
    def authenticate(username, password):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM User WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        conn.close()
        if user:
           return User(*user)
        else:
           return None

    @staticmethod
    def add_user(name, phone_number, age, username, password):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO User (name, phone_number, age, username, password) VALUES (?, ?, ?, ?, ?)",
                    (name, phone_number, age, username, password))
        conn.commit()
        conn.close()




#     def save(self):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         sql = f"""
#             INSERT INTO {self.TABLE_NAME} (name, phone_number, age, Food_id)
#             VALUES (?, ?, ?, ?)
#         """
#         cursor.execute(sql, (self.name, self.phone_number, self.age, self.Food_id))
#         conn.commit()
#         self.id = cursor.lastrowid
#         return self

#     def dictionary(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "phone_number": self.phone_number,
#             "age": self.age
#         }

#     @classmethod
#     def using_the_phone(cls, phone):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         sql = f"""
#             SELECT * FROM {cls.TABLE_NAME}
#             WHERE phone_number = ?
#         """
#         row = cursor.execute(sql, (phone,)).fetchone()
#         return cls.row_to_instance(row)

#     @classmethod
#     def row_to_instance(cls, row):
#         if row is None:
#             return None
#         user = cls(None, row[1], row[2], row[3], row[4])
#         user.id = row[0]
#         return user


#     def update(self):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         sql = f"""
#             UPDATE {self.TABLE_NAME} SET name=?, phone_number=?, age=?, Food_id=? WHERE id=?
#         """
#         cursor.execute(sql, (self.name, self.phone_number, self.age, self.Food_id, self.id))
#         conn.commit()
#         print(f"{self.name} updated")

#     def delete(self):
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         sql = f"""
#             DELETE FROM {self.TABLE_NAME} WHERE id = ?
#         """
#         cursor.execute(sql, (self.id,))
#         conn.commit()
#         print(f"{self.name} deleted")

# User.create_table()
