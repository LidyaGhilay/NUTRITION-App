from models.Nutritionist import Nutritionist
from models.User import User
from models.Food import Food
from database.setup import create_table, insert_initial_foods

def main():
    create_table()  # Ensure tables are created if they don't exist
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
        name = input("Your Name: ")
        phone_number = input("Phone Number: ")
        age = input("Age: ")
        username = input("Username: ")
        password = input("Password: ")
        
        existing_user = User.find_by_username(username)
        if existing_user:
            print("Username already exists. Please choose a different username.")
            continue
        
        new_user = User(None, name, phone_number, age, username, password)
        new_user.save()
        
        print("Registration successful!")
        break  # Exit loop after successful registration

def handle_register_nutritionist():
    while True:
        print("\nRegister as a Nutritionist")
        name = input("Your Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        consultation_fee = input("Consultation Fee: ")
        password = input("Password: ")

        Nutritionist.add_nutritionist(name, phone_number, email, consultation_fee, password)
        print("Registration successful!")
        break  # Exit loop after successful registration

def handle_login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
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
        print("2. Update Client Information")
        print("3. Schedule Consultations")
        print("4. View Client Progress")
        print("5. Manage Meal Plans")
        print("6. Send Messages or Recommendations")
        print("7. Access Nutrition Resources")
        print("8. Log out")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            view_client_list(nutritionist)
        elif choice == "2":
            update_client_info(nutritionist)
        elif choice == "3":
            schedule_consultations(nutritionist)
        elif choice == "4":
            view_client_progress(nutritionist)
        elif choice == "5":
            manage_meal_plans(nutritionist)
        elif choice == "6":
            send_messages(nutritionist)
        elif choice == "7":
            access_nutrition_resources()
        elif choice == "8":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def view_client_list(nutritionist):
    # Placeholder for functionality to view client list
    pass

def update_client_info(nutritionist):
    # Placeholder for functionality to update client information
    pass

def schedule_consultations(nutritionist):
    # Placeholder for functionality to schedule consultations
    pass

def view_client_progress(nutritionist):
    # Placeholder for functionality to view client progress
    pass

def manage_meal_plans(nutritionist):
    # Placeholder for functionality to manage meal plans
    pass

def send_messages(nutritionist):
    # Placeholder for functionality to send messages or recommendations
    pass

def access_nutrition_resources():
    # Placeholder for functionality to access nutrition resources
    pass

if __name__ == '__main__':
    main()
