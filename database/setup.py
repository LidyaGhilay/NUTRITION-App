# database/setup.py

import sqlite3
from database.connection import get_db_connection

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create User table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL UNIQUE,
        age TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # Create Nutritionist table
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

    # Create Food table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Food (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        calories REAL NOT NULL,
        description TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Drop existing Food table (for development/testing purposes only)
    cursor.execute("DROP TABLE IF EXISTS Food")

    # Create Food table with description column
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Food (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        calories REAL NOT NULL,
        description TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def insert_initial_foods():
    conn = get_db_connection()
    cursor = conn.cursor()

    foods = [
        ("Apple", "Fruit", 52, "A delicious apple packed with nutrients."),
        ("Banana", "Fruit", 105, "Energizing and full of potassium."),
        ("Chicken Breast", "Meat", 165, "Lean protein source, great for muscle building."),
        ("Salmon", "Fish", 206, "Rich in omega-3 fatty acids, good for heart health."),
        ("Spinach", "Vegetable", 23, "Nutrient-dense leafy green, high in iron and vitamins."),
        ("Quinoa", "Grain", 222, "Protein-rich ancient grain, gluten-free."),
        ("Greek Yogurt", "Dairy", 59, "High in protein and probiotics, good for gut health."),
        ("Almonds", "Nut", 7, "Rich in healthy fats and vitamin E."),
        ("Oatmeal", "Grain", 68, "Fiber-rich whole grain, great for breakfast."),
        ("Avocado", "Fruit", 160, "Creamy and nutritious, high in healthy fats.")
    ]

    cursor.executemany("INSERT INTO Food (name, category, calories, description) VALUES (?, ?, ?, ?)", foods)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_initial_foods()