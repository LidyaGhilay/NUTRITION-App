import sqlite3
from database.setup import create_table, insert_initial_foods
from database.connection import get_db_connection
from models.Nutritionist import Nutritionist
from models.User import User
from models.Food import Food

class Style:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def main():
    create_table()  
    insert_initial_foods() 

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
    print(f"\n{Style.HEADER + Style.BOLD}Nutri-App-CLI{Style.END}")  
    print(f"{Style.OKBLUE}Welcome to Nutritionist App!{Style.END}")  
    print("\nSelect an option:")
    print(f"{Style.OKGREEN}1. Register as a User{Style.END}")  
    print(f"{Style.OKGREEN}2. Register as a Nutritionist{Style.END}")  
    print(f"{Style.OKGREEN}3. Login{Style.END}") 
    print(f"{Style.FAIL}4. Exit{Style.END}") 

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
            break  
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
            break  
        except Exception as e:
            print(f"{Style.FAIL}Error: {e}{Style.END}")
            break

def handle_login():
    while True:
        print(f"\n\033[91mback\033[0m at any time to return to the main menu.")

        username = input("\nEnter your username: ")
        if username.lower() == 'back':
            return
        
        password = input("Enter your password: ")
        if password.lower() == 'back':
            return
        
        user = User.authenticate(username, password)
        nutritionist = Nutritionist.authenticate(username, password)

        if user:
            print(f"\nLogged in as user: {user.name}")
            user_menu(user)
            break  
        elif nutritionist:
            print(f"\nLogged in as nutritionist: {nutritionist.name}")
            nutritionist_menu(nutritionist)
            break  
        else:
            print(f"\nInvalid username or password")

def user_menu(user):
    while True:
        print("\nSelect an option:")
        print(f"{Style.OKGREEN}1. View Available Foods{Style.END}")  
        print(f"{Style.OKGREEN}2. Update Password{Style.END}") 
        print(f"{Style.FAIL}3. Back to Main Menu{Style.END}")  
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
        print(f"{Style.OKGREEN}1. View Client List{Style.END}")  
        print(f"{Style.OKBLUE}2. Consultation Date{Style.END}")  
        print(f"{Style.OKBLUE}3. View Client Progress{Style.END}")  
        print(f"{Style.OKGREEN}4. Update Password{Style.END}")  
        print(f"{Style.FAIL}5. Back to Main Menu{Style.END}")  

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            handle_view_client_list(nutritionist)
        elif choice == "2":
            handle_enter_consultation_date(nutritionist)
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
    client_data = [
        {"name": "John Doe", "progress": "Making good progress"},
        {"name": "Rose lyn", "progress": "Needs more improvement"},
        {"name": "Bonito Zerom", "progress": "No progress data available"}  
    ]

    print(f"\n{Style.BOLD}Client Progress:{Style.END}")
    for client in client_data:
        print(f"{Style.OKBLUE}Client: {client['name']}, Progress: {client['progress']}{Style.END}")

def handle_view_client_list(nutritionist):
    clients = [
        {"name": "John Doe", "phone_number": "123-456-7890", "email": "client_a@example.com"},
        {"name": "Rose lyn", "phone_number": "234-567-8901", "email": "client_b@example.com"},
        {"name": "Bonito Zerom", "phone_number": "345-678-9012", "email": "client_c@example.com"},
    ]

    if clients:
        print(f"\n{Style.BOLD}Client List for {nutritionist.name}:{Style.END}")
        for client in clients:
            print(f"{Style.OKBLUE}Client Name: {client['name']}, Phone Number: {client['phone_number']}, Email: {client['email']}{Style.END}")
    else:
        print(f"{Style.FAIL}No clients found.{Style.END}")

def handle_enter_consultation_date(nutritionist):
    clients = [
        {"name": "John Doe"},
        {"name": "Rose lyn"},
        {"name": "Bonito Zerom"}
    ]

    print(f"\n{Style.BOLD}Select a client:{Style.END}")
    for idx, client in enumerate(clients, start=1):
        print(f"{idx}. {client['name']}")

    choice = input(f"\nEnter client's number (1-{len(clients)}): ")
    try:
        client_index = int(choice) - 1
        if 0 <= client_index < len(clients):
            client_name = clients[client_index]['name']
            consultation_date = input("Enter consultation date (YYYY-MM-DD): ")

            print(f"Consultation date {consultation_date} recorded for client {client_name}")
        else:
            print(f"{Style.FAIL}Invalid client number. Please choose a valid option.{Style.END}")
    except ValueError:
        print(f"{Style.FAIL}Invalid input. Please enter a number.{Style.END}")

def update_nutritionist_password(nutritionist):
    new_password = input("Enter new password: ")
    nutritionist.password = new_password
    nutritionist.save()
    print(f"{Style.OKGREEN}Password updated for nutritionist: {nutritionist.name}{Style.END}")

if __name__ == "__main__":
    main()
    
