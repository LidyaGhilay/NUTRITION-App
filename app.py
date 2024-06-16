import sqlite3
from database.setup import create_table, insert_initial_foods
from database.connection import get_db_connection
from models.Nutritionist import Nutritionist
from models.User import User
from models.Food import Food

def main():
    create_table()  # Ensure tables are created if they don't exist
    insert_initial_foods()  # Insert initial data into tables

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            handle_register_user()
        elif choice == "2":
            handle_register_nutritionist()
        elif choice == "3":
            handle_login()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def print_menu():
    print("\nNutri-App-CLI")
    print("Welcome to Nutritionist App!")
    print("Select an option:")
    print("1. Register as a User")
    print("2. Register as a Nutritionist")
    print("3. Login")
    print("4. Exit")

def handle_register_user():
    while True:
        print("\nRegister as a User")
        print("Enter 'back' to return to main menu.")
        name = input("Your Name: ")
        if name.lower() == 'back':
            return
        
        phone_number = input("Phone Number: ")
        if phone_number.lower() == 'back':
            return
        
        age = input("Age: ")
        if age.lower() == 'back':
            return
        
        username = input("Username: ")
        if username.lower() == 'back':
            return
        
        password = input("Password: ")
        if password.lower() == 'back':
            return

        existing_user = User.find_by_username(username)
        if existing_user:
            print("Username already exists. Please choose a different username.")
            continue
        
        new_user = User(None, name, phone_number, age, username, password)
        try:
            new_user.save()
            print("Registration successful!")
            break  # Exit loop after successful registration
        except Exception as e:
            print(f"Error: {e}")
            break

def handle_register_nutritionist():
    while True:
        print("\nRegister as a Nutritionist")
        print("Enter 'back' to return to main menu.")
        name = input("Your Name: ")
        if name.lower() == 'back':
            return
        
        phone_number = input("Phone Number: ")
        if phone_number.lower() == 'back':
            return
        
        email = input("Email: ")
        if email.lower() == 'back':
            return
        
        consultation_fee = input("Consultation Fee: ")
        if consultation_fee.lower() == 'back':
            return
        
        password = input("Password: ")
        if password.lower() == 'back':
            return

        existing_nutritionist = Nutritionist.find_by_phone_number(phone_number)
        if existing_nutritionist:
            print("A nutritionist with this phone number already exists.")
            continue

        try:
            Nutritionist.add_nutritionist(name, phone_number, email, consultation_fee, password)
            print("Registration successful!")
            break  # Exit loop after successful registration
        except Exception as e:
            print(f"Error: {e}")
            break

def handle_login():
    while True:
        username = input("Enter your username: ")
        if username.lower() == 'back':
            return
        
        password = input("Enter your password: ")
        if password.lower() == 'back':
            return
        
        user = User.authenticate(username, password)
        nutritionist = Nutritionist.authenticate(username, password)

        if user:
            print(f"Logged in as user: {user.name}")
            user_menu(user)
            break  # Exit loop after successful login
        elif nutritionist:
            print(f"Logged in as nutritionist: {nutritionist.name}")
            nutritionist_menu(nutritionist)
            break  # Exit loop after successful login
        else:
            print("Invalid username or password")

def user_menu(user):
    while True:
        print("\nSelect an option:")
        print("1. View Available Foods")
        print("2. Update Password")
        print("3. Back to Main Menu")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            list_available_foods()
        elif choice == "2":
            update_user_password(user)
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def list_available_foods():
    foods = Food.get_all_foods()
    if foods:
        print("\nAvailable Foods:")
        for food in foods:
            print(f"Name: {food.name}, Category: {food.category}, Calories: {food.calories}, Description: {food.description}")
    else:
        print("No foods available.")

def update_user_password(user):
    new_password = input("Enter new password: ")
    user.password = new_password
    user.save()
    print(f"Password updated for user: {user.username}")

def nutritionist_menu(nutritionist):
    while True:
        print(f"\nLogged in as nutritionist: {nutritionist.name}")
        print("Select an option:")
        print("1. View Client List")
        print("2. Consultation Date")
        print("3. View Client Progress")
        print("4. Update Password")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            handle_view_client_list(nutritionist)
        elif choice == "2":
            enter_consultation_date(nutritionist)
        elif choice == "3":
            view_client_progress(nutritionist)
        elif choice == "4":
            update_nutritionist_password(nutritionist)
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def handle_view_client_list(nutritionist):
    clients = nutritionist.get_client_list()
    if clients:
        print("\nClient List:")
        for client in clients:
            print(f"Name: {client['name']}, Phone Number: {client['phone_number']}, Email: {client['email']}")
    else:
        print("No clients found.")

if __name__ == "__main__":
    main()
