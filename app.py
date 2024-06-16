# Importing necessary libraries
import sqlite3
from database.setup import create_table, insert_initial_foods
from database.connection import get_db_connection
from models.Nutritionist import Nutritionist
from models.User import User
from models.Food import Food

# ANSI escape sequences for text styling
class Style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Function definitions
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
            print(f"\n{Style.WARNING}Exiting...{Style.END}")
            break
        else:
            print(f"\n{Style.FAIL}Invalid choice. Please choose a valid option.{Style.END}")

def print_menu():
    print(f"\n{Style.HEADER + Style.BOLD}Nutri-App-CLI{Style.END}")  # Bold and magenta header
    print(f"{Style.OKBLUE}Welcome to Nutritionist App!{Style.END}")  # Blue subtitle
    print("\nSelect an option:")
    print(f"{Style.OKGREEN}1. Register as a User{Style.END}")  # Green options
    print(f"{Style.OKGREEN}2. Register as a Nutritionist{Style.END}")  # Green options
    print(f"{Style.OKGREEN}3. Login{Style.END}")  # Green options
    print(f"{Style.FAIL}4. Exit{Style.END}")  # Red option

def handle_register_user():
    while True:
        print(f"\n{Style.BOLD}Register as a User{Style.END}")
        print(f"Enter '{Style.FAIL}back{Style.END}' to return to main menu.")
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
            print(f"{Style.FAIL}Username already exists. Please choose a different username.{Style.END}")
            continue
        
        new_user = User(None, name, phone_number, age, username, password)
        try:
            new_user.save()
            print(f"{Style.OKGREEN}Registration successful!{Style.END}")
            break  # Exit loop after successful registration
        except Exception as e:
            print(f"{Style.FAIL}Error: {e}{Style.END}")
            break

def handle_register_nutritionist():
    while True:
        print(f"\n{Style.BOLD}Register as a Nutritionist{Style.END}")
        print(f"Enter '{Style.FAIL}back{Style.END}' to return to main menu.")
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
            print(f"{Style.FAIL}A nutritionist with this phone number already exists.{Style.END}")
            continue

        try:
            Nutritionist.add_nutritionist(name, phone_number, email, consultation_fee, password)
            print(f"{Style.OKGREEN}Registration successful!{Style.END}")
            break  # Exit loop after successful registration
        except Exception as e:
            print(f"{Style.FAIL}Error: {e}{Style.END}")
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
            print(f"{Style.FAIL}Invalid username or password{Style.END}")

def user_menu(user):
    while True:
        print("\nSelect an option:")
        print(f"{Style.OKGREEN}1. View Available Foods{Style.END}")  # Green option
        print(f"{Style.OKGREEN}2. Update Password{Style.END}")  # Green option
        print(f"{Style.FAIL}3. Back to Main Menu{Style.END}")  # Red option
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            list_available_foods()
        elif choice == "2":
            update_user_password(user)
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print(f"{Style.FAIL}Invalid choice. Please choose a valid option.{Style.END}")

def list_available_foods():
    foods = Food.get_all_foods()
    if foods:
        print(f"\n{Style.BOLD}Available Foods:{Style.END}")
        for food in foods:
            print(f"{Style.OKBLUE}Name: {food.name}, Category: {food.category}, Calories: {food.calories}, Description: {food.description}{Style.END}")
    else:
        print(f"{Style.FAIL}No foods available.{Style.END}")

def update_user_password(user):
    new_password = input("Enter new password: ")
    user.password = new_password
    user.save()
    print(f"{Style.OKGREEN}Password updated for user: {user.username}{Style.END}")

def nutritionist_menu(nutritionist):
    while True:
        print(f"\n{Style.BOLD}Logged in as nutritionist: {nutritionist.name}{Style.END}")
        print("\nSelect an option:")
        print(f"{Style.OKGREEN}1. View Client List{Style.END}")  # Green option
        print(f"{Style.OKBLUE}2. Consultation Date{Style.END}")  # Blue option
        print(f"{Style.OKBLUE}3. View Client Progress{Style.END}")  # Blue option
        print(f"{Style.OKGREEN}4. Update Password{Style.END}")  # Green option
        print(f"{Style.FAIL}5. Back to Main Menu{Style.END}")  # Red option

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
            print(f"{Style.FAIL}Invalid choice. Please choose a valid option.{Style.END}")

def view_client_progress(nutritionist):
    # Simulated client progress data (replace with actual database interaction)
    client_data = [
        {"name": "Client A", "progress": "Making good progress"},
        {"name": "Client B", "progress": "Needs more improvement"},
        {"name": "Client C", "progress": "No progress data available"}
        # Add more client entries as needed
    ]

    # Display client progress
    print(f"\n{Style.BOLD}Client Progress:{Style.END}")
    for client in client_data:
        print(f"{Style.OKBLUE}Client: {client['name']}, Progress: {client['progress']}{Style.END}")



def handle_view_client_list(nutritionist):
    # Simulated client data
    clients = [
        {"name": "Client A", "phone_number": "123-456-7890", "email": "client_a@example.com"},
        {"name": "Client B", "phone_number": "234-567-8901", "email": "client_b@example.com"},
        {"name": "Client C", "phone_number": "345-678-9012", "email": "client_c@example.com"},
    ]

    if clients:
        print(f"\n{Style.BOLD}Client List for {nutritionist.name}:{Style.END}")
        for client in clients:
            print(f"{Style.OKBLUE}Client Name: {client['name']}, Phone Number: {client['phone_number']}, Email: {client['email']}{Style.END}")
    else:
        print(f"{Style.FAIL}No clients found.{Style.END}")


    def enter_consultation_date(nutritionist):
    client_name = input("Enter client's name: ")
    consultation_date = input("Enter consultation date (YYYY-MM-DD): ")

    # Simulated update process (replace with actual database interaction)
    client_found = False
    for client in nutritionist.clients:
        if client.name == client_name:
            client.consultation_date = consultation_date
            client_found = True
            break
    
    if client_found:
        print(f"Consultation date {consultation_date} recorded for client {client_name}")
    else:
        print(f"{Style.FAIL}Client '{client_name}' not found.{Style.END}")


if __name__ == "__main__":
    main()
