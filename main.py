from ME.access import Account

user_account = Account()
error = "Invalid input. Please enter valid data."
logged_in_username = ""
while True:
    while True:
        print("\noptions")
        print("1. Sign up")
        print("2. Log in")
        print("3, Forget password")
        if logged_in_username:
            print(f"Logged in as {logged_in_username}")
            print("4. Edit account")
            print("5. Password edit")
        print("6. Exit")
        choice = input ("Enter your choice: ")
        if choice == '1':
            while True:
                print("Create an account with us")
                try:
                    username = input("Enter username: ")
                    while True:
                        password = input("Create password: ")
                        vali = user_account.validate_password(password)
                        if vali:
                            break
                        else:
                            print("Incomplete characters in the password..")
                    email = input("Enter your email address: ") + "@gmail.com"
                    name = input("Enter full name: ")
                    age = int(input("Enter age: "))
                    mobile = int(input("Enter phone number: "))
                    address = input("Enter address: ")
                except ValueError:
                    print(error)
                except FileNotFoundError:
                    print(error)
                else:
                    sign = user_account.sign_up(username, password, email, name, age, address, mobile)
                    if sign:
                        print("Account created successfully.")
                        break
        elif choice == '2':
            while True:
                print("Log in")
                try:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                except ValueError:
                    print(error)
                else:
                    logged_in_username = user_account.login(username, password)
                    if logged_in_username:
                        print(f"Welcome, {logged_in_username}!")
                        break
                    print("Login attempt failed.")
            break
        elif choice == '3':
            while True:
                print("Forget password")
                username = input("Enter your username: ")
                reset = user_account.forget(username)
                if reset is True:
                    break
                break       
        elif choice == '4'and logged_in_username:
            while True:
                print("Editing info for user:")
                try:
                    if not username:
                        print("You must be logged in to edit account information.")
                        break
                    name = input(f"Enter new name ({username}): ")
                    email = input("Enter new email or leave it empty: ") + "@gmail.com"
                    age = int(input("New age: "))
                    mobile = int(input("Enter new mobile number: "))
                    address = input("New address: ")
                    password = input("Enter your previous password to confirm the update: ")
                except FileNotFoundError:
                    print("User file not found. Please check your username.")
                except ValueError:
                    print(error)
                else:
                    edit = user_account.edit_info(username, password, email, name, age, address, mobile)
                    if edit:
                        print("Edit account information successful.")
                        break
                    break
        elif choice == '5' and logged_in_username:
            while True:
                old_password = input("Enter your old password: ")
                user_account.password_edit(logged_in_username, old_password)
                break
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")