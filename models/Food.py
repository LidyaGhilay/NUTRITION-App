# models/Food.py

from database.connection import get_db_connection

class Food:
    def __init__(self, id, name, category, calories, description):
        self.id = id
        self.name = name
        self.category = category
        self.calories = calories
        self.description = description
          # Ensure this matches the column name in your database
    
    @classmethod
    def get_all_foods(cls):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Food")
        foods = cursor.fetchall()

        conn.close()

        return [cls(*food) for food in foods]

    # Add other methods as needed, such as saving a new food item, updating, deleting, etc.
