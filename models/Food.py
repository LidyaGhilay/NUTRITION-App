from db import get_db_connection

class Food:
    TABLE_NAME = "Food"

    def __init__(self, id, name, category, calories, description, Nutri_id):
        self.id = id
        self.name = name
        self.category = category
        self.calories = calories
        self.description = description
        self.Nutri_id = Nutri_id

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name, category, calories, descriptions, Nutri_id)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.category, self.calories, self.description, self.Nutri_id))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"{self.name} saved")

    def update(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            UPDATE {self.TABLE_NAME} SET name=?, category=?, calories=?, descriptions=?, Nutri_id=? WHERE id=?
        """
        cursor.execute(sql, (self.name, self.category, self.calories, self.description, self.Nutri_id, self.id))
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

    @classmethod
    def create_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              category TEXT NOT NULL,
              calories REAL NOT NULL,
              descriptions TEXT NOT NULL,
              Nutri_id INTEGER,
              FOREIGN KEY (Nutri_id) REFERENCES Nutritionist(id)
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Food table created")
