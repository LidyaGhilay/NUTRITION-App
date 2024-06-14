from models.Nutritionist import Nutritionist
from models.User import User
from database.setup import create_table 

def menu():
    create_table()

    print("Nutri-App-CLI")
    print("Welcome to Nutritionist App!")
    print("1. Register as a User")
    print("2. Register as a Nutritionist")
    print("3. Login")
    print("4. Exit")

def add_user():
    name = input("Your Name:")
    phone_number = input("Phone Number:")
    age = input("Age:")
    username = input("Username:")
    password = input("Password:")
    User.add_user(name, phone_number, age, username, password)
    print("User added successfully!")

def add_nutritionist():
    name = input("Your Name:")
    phone_number = input("Phone Number:")
    email = input("Give your Email:")
    consultation_fee = input("Consultation Fee:")
    password = input("Password:")
    Nutritionist.add_nutritionist(name, phone_number, email, consultation_fee, password)
    print("You've Registered as a Nutritionist")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Check if it's a user or a nutritionist logging in
    user = User.authenticate(username, password)
    nutritionist = Nutritionist.authenticate(username, password)

    if user:
        print("Logged in as user:", user.name)
        # Add user-specific functionality here
    elif nutritionist:
        print("Logged in as nutritionist:", nutritionist.name)
        # Add nutritionist-specific functionality here
    else:
        print("Invalid username or password")

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
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

