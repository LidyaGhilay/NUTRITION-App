import sqlite3
from database.connection import get_db_connection

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create User table if not exists
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

    # Create Nutritionist table if not exists
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

    # Create Client table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Client (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL UNIQUE,
        email TEXT,
        nutritionist_id INTEGER NOT NULL,
        FOREIGN KEY (nutritionist_id) REFERENCES Nutritionist (id)
    )
    """)

    # Create Food table if not exists
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

    # Insert initial Food data if not exists
    cursor.execute("SELECT COUNT(*) FROM Food")
    count = cursor.fetchone()[0]
    if count == 0:
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

    # Insert initial Nutritionist data if not exists
    cursor.execute("SELECT COUNT(*) FROM Nutritionist")
    count = cursor.fetchone()[0]
    if count == 0:
        nutritionists = [
            ("John Doe", "123-456-7890", "john@example.com", 50.0, "password1"),
            ("Jane Smith", "987-654-3210", "jane@example.com", 70.0, "password2")
        ]

        cursor.executemany("INSERT INTO Nutritionist (name, phone_number, email, consultation_fee, password) VALUES (?, ?, ?, ?, ?)", nutritionists)

   
    cursor.execute("SELECT COUNT(*) FROM Client")
    count = cursor.fetchone()[0]
    if count == 0:
        clients = [
            ("Client A", "111-222-3333", "clientA@example.com", 1),
            ("Client B", "444-555-6666", "clientB@example.com", 1),
            ("Client C", "777-888-9999", "clientC@example.com", 2)
        ]

        cursor.executemany("INSERT INTO Client (name, phone_number, email, nutritionist_id) VALUES (?, ?, ?, ?)", clients)

    conn.commit()
    conn.close()

def fetch_clients():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT c.name AS client_name, c.phone_number AS client_phone, c.email AS client_email,
                   n.name AS nutritionist_name, n.phone_number AS nutritionist_phone, n.email AS nutritionist_email
            FROM Client c
            INNER JOIN Nutritionist n ON c.nutritionist_id = n.id
        """)
        clients = cursor.fetchall()
        return clients
    except Exception as e:
        print(f"Error fetching clients: {e}")
        return []
    finally:
        conn.close()

if __name__ == "__main__":
    create_table()
    insert_initial_foods()

    # Fetch and print clients for verification
    clients = fetch_clients()
    print("\nClient Table Contents:")
    for client in clients:
        print(client)
