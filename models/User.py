import sqlite3

def get_db_connection():
    return sqlite3.connect('database.db')

class User:
    TABLE_NAME = "userDetails"

    def __init__(self, id, name, phone_number, age, Food_id):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.Food_id = Food_id

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name, phone_number, age, Food_id)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.phone_number, self.age, self.Food_id))
        conn.commit()
        self.id = cursor.lastrowid
        return self

    def dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "age": self.age
        }

    @classmethod
    def using_the_phone(cls, phone):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
            WHERE phone_number = ?
        """
        row = cursor.execute(sql, (phone,)).fetchone()
        return cls.row_to_instance(row)

    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        user = cls(None, row[1], row[2], row[3], row[4])
        user.id = row[0]
        return user

    @classmethod
    def create_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              phone_number TEXT NOT NULL UNIQUE,
              age TEXT NOT NULL,
              Food_id INTEGER,
              FOREIGN KEY (Food_id) REFERENCES Food(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Users table created")

    def update(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            UPDATE {self.TABLE_NAME} SET name=?, phone_number=?, age=?, Food_id=? WHERE id=?
        """
        cursor.execute(sql, (self.name, self.phone_number, self.age, self.Food_id, self.id))
        conn.commit()
        print(f"{self.name} updated")

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            DELETE FROM {self.TABLE_NAME} WHERE id = ?
        """
        cursor.execute(sql, (self.id,))
        conn.commit()
        print(f"{self.name} deleted")

User.create_table()
