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

    def get_client_list(self):
        conn = get_db_connection()
        cur = conn.cursor()

        try:
            cur.execute("SELECT * FROM Client WHERE nutritionist_id = ?", (self.id,))
            clients = cur.fetchall()

            client_list = []
            for client in clients:
                client_dict = {
                    'id': client[0],
                    'name': client[1],
                    'phone_number': client[2],
                    'email': client[3]
                    # Add more fields as needed
                }
                client_list.append(client_dict)

            return client_list
        except Exception as e:
            print(f"Error fetching clients: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def find_by_phone_number(phone_number):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Nutritionist WHERE phone_number = ?", (phone_number,))
        nutritionist = cur.fetchone()
        conn.close()
        if nutritionist:
            return Nutritionist(*nutritionist)
        else:
            return None

    @staticmethod
    def add_nutritionist(name, phone_number, email, consultation_fee, password):
        conn = get_db_connection()
        cur = conn.cursor()

        try:
            cur.execute("SELECT * FROM Nutritionist WHERE phone_number = ?", (phone_number,))
            existing_nutritionist = cur.fetchone()

            if existing_nutritionist:
                print(f"Nutritionist with phone number '{phone_number}' already exists.")
            else:
                cur.execute("INSERT INTO Nutritionist (name, phone_number, email, consultation_fee, password) VALUES (?, ?, ?, ?, ?)",
                            (name, phone_number, email, consultation_fee, password))
                conn.commit()
                print("Nutritionist registered successfully.")
        except Exception as e:
            print(f"Error adding nutritionist: {e}")
        finally:
            conn.close()

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
