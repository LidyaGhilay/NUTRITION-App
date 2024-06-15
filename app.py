from models.Nutritionist import Nutritionist
from models.User import User
from models.Food import Food
from database.setup import create_table 
from database.setup import insert_initial_foods
def main():
    create_table()  # Ensure tables are created if they don't exist
    insert_initial_foods()
    while True:
        print("\nNutri-App-CLI")
        print("Welcome to Nutritionist App!")
        print("Select an option:")
        print("1. Register as a User")
        print("2. Register as a Nutritionist")
        print("3. Login")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_nutritionist()
        elif choice == "3":
            login()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


def add_user():
    print("\nRegister as a User")
    name = input("Your Name: ")
    phone_number = input("Phone Number: ")
    age = input("Age: ")
    username = input("Username: ")
    password = input("Password: ")
    
    existing_user = User.find_by_username(username)
    if existing_user:
        print("Username already exists. Please choose a different username.")
        return
    
    new_user = User(None, name, phone_number, age, username, password)
    new_user.save()
    
    print("Registration successful!")

def add_nutritionist():
    print("\nRegister as a Nutritionist")
    name = input("Your Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    consultation_fee = input("Consultation Fee: ")
    password = input("Password: ")

    Nutritionist.add_nutritionist(name, phone_number, email, consultation_fee, password)
    print("Registration successful!")

def list_available_foods():
    print("Available Foods:")
    foods = Food.get_all_foods()
    if foods:
        for food in foods:
            print(f"Name: {food.name}, Category: {food.category}, Calories: {food.calories}, Description: {food.description}")
    else:
        print("No foods available.")
def update_user():
    username = input("\nEnter your username: ")
    password = input("Enter your current password: ")
    
    user = User.authenticate(username, password)
    
    if user:
        new_password = input("Enter new password: ")
        user.password = new_password
        user.save()
        print(f"Password updated for user: {username}")
    else:
        print("Invalid username or password.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user = User.authenticate(username, password)
    nutritionist = Nutritionist.authenticate(username, password)

    if user:
        print("Logged in as user:", user.name)
        while True:
            print("\nSelect an option:")
            print("1. View Available Foods")
            print("2. Log out")
            choice = input("Enter your choice (1-2): ")

            if choice == "1":
                list_available_foods()
            elif choice == "2":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    elif nutritionist:
        print("Logged in as nutritionist:", nutritionist.name)
        # Add nutritionist-specific functionality here
    else:
        print("Invalid username or password")

if __name__ == '__main__':
    main()
#  def main():
    
#     User.create_table()
#     Nutritionist.create_table()
#     Food.create_table()

#     parser = argparse.ArgumentParser(description='CLI Application for managing users')
#     subparsers = parser.add_subparsers(dest='command', help='sub-command help')

   

#     args = parser.parse_args()

#     if args.command == 'add_user':
#         add_user()
#     elif args.command == 'list_users':
#         list_users()
   

# 

# def list_users():
#     users = User.find()
#     for user in users:
#         print(user)

# def update_user(user_id, name, phone_number, age, food_id):
#     user = User(user_id, name, phone_number, age, food_id)
#     user.update()
#     print("User updated successfully.")

# def delete_user(user_id):
#     user = User.row_to_instance(User.find_by_id(user_id))
#     if user:
#         user.delete()
#         print("User deleted successfully.")
#     else:
#         print("User not found.")

# def main():
#     parser = argparse.ArgumentParser(description='CLI Application for managing users')
#     subparsers = parser.add_subparsers(dest='command', help='sub-command help')

   
#     add_user_parser = subparsers.add_parser('add_user', help='Add a new user')
#     add_user_parser.add_argument('name', type=str, help='User name')
#     add_user_parser.add_argument('phone_number', type=str, help='User phone number')
#     add_user_parser.add_argument('age', type=str, help='User age')
#     add_user_parser.add_argument('food_id', type=int, help='Food ID')

    
#     subparsers.add_parser('list_users', help='List all users')

    
#     update_user_parser = subparsers.add_parser('update_user', help='Update an existing user')
#     update_user_parser.add_argument('user_id', type=int, help='User ID')
#     update_user_parser.add_argument('name', type=str, help='User name')
#     update_user_parser.add_argument('phone_number', type=str, help='User phone number')
#     update_user_parser.add_argument('age', type=str, help='User age')
#     update_user_parser.add_argument('food_id', type=int, help='Food ID')

#     # Command: delete_user
#     delete_user_parser = subparsers.add_parser('delete_user', help='Delete an existing user')
#     delete_user_parser.add_argument('user_id', type=int, help='User ID')

#     args = parser.parse_args()

#     if args.command == 'add_user':
#         add_user(args.name, args.phone_number, args.age, args.food_id)
#     elif args.command == 'list_users':
#         list_users()
#     elif args.command == 'update_user':
#         update_user(args.user_id, args.name, args.phone_number, args.age, args.food_id)
#     elif args.command == 'delete_user':
#         delete_user(args.user_id)

