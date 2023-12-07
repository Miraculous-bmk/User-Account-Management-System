import hashlib
import random
import os
import re
class Account:
    def __init__(self):
        self.username = ""
        self.password = ""
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    def sign_up(self, username, password, email, name, age, address, mobile):
        main_file = username + ".User.txt"
        hashed_password = self.hash_password(password)
        with open(main_file, 'w') as file:
            file.write(username + "\n")
            file.write(f"Password: {hashed_password}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Mobile: {mobile}\n") 
        return True
    def login(self, username, password):
        try:
            main_file = f"{username}.User.txt"
            if not os.path.exists(main_file):
                print("User not found. Please check your username.")
                return None
            with open(main_file, 'r') as file:
                lines = file.readlines()
            if not len(lines) >= 2:
                ("Invalid user file format. Cannot retrieve password.")
                return None                
            stored_password = lines[1].strip().split(": ")[1]
            entered_password = hashlib.sha256(password.encode()).hexdigest()
            if entered_password == stored_password:
                print("Login successful.")
                return username
            else:
                print("Incorrect password. Login failed.")
                return None
        except FileNotFoundError and Exception:
            print("User file not found or Error during login. Please check your username.")
            return None
    def validate_password(self, password):
        if len(password) < 8:
            print("Make sure your password is at least 8 characters.")
            return False
        if not re.search(r'\d', password):
            print("Make sure your password has at least 1 number.")
            return False
        if not re.search(r'[A-Z]', password):
            print("Make sure your password has at least 1 capital letter.")
            return False
        if not re.search(r'[!@#$%^&*]', password):
            print("Make sure your password includes special characters.")
            return False
        return True
    def forget(self, username):
        try:
            inputin = username
            if inputin is not None:
                main_file = username + ".User.txt"
                if not os.path.exists(main_file):
                    print("User file not found. Please check your username.")
                    return
                reset_code = str(random.randint(1000, 9999))
                print(f"A code has been generated to reset your password: {reset_code}")
                code = input("Enter the code you received: ")
                if code != reset_code:
                    print("Incorrect code. Password reset failed.")
                    return
                new_password = input("Enter a new password: ")
                if not self.validate_password(new_password):  
                    print("Invalid password format. Password reset failed.")
                    return
                with open(main_file, 'r+') as file:
                    lines = file.readlines()
                    if len(lines) >= 2:
                        lines[1] = f"Password: {self.hash_password(new_password)}\n"
                        file.seek(0)
                        file.writelines(lines)
                        file.truncate()
                        print("Password updated successfully.")
                    else:
                        print("Invalid user file format. Cannot retrieve password.")
            else:
                print("Username not found.")
        except FileNotFoundError and Exception:
            print("User file not found or Error. Please check your username.")
    def edit_info(self, username, password, email, name, address, age, mobile):
        try:
            main_file = username + ".User.txt"
            with open(main_file, 'r+') as file:
                lines = file.readlines()
                stored_password = lines[1].strip().split(": ")[1]
                entered_password = hashlib.sha256(password.encode()).hexdigest()
                if entered_password != stored_password:
                    print("Password update failed. Please provide the correct previous password.")
                    return
                updated_lines = []
                for line in lines:
                    if line.startswith("Email:"):
                        updated_lines.append(f"Email: {email}\n")
                    elif line.startswith("Name:"):
                        updated_lines.append(f"Name: {name}\n")
                    elif line.startswith("Age:"):
                        updated_lines.append(f"Age: {age}\n")
                    elif line.startswith("Mobile:"):
                        updated_lines.append(f"Mobile: {mobile}\n")
                    elif line.startswith("Address:"):
                        updated_lines.append(f"Address: {address}\n")
                    else:
                        updated_lines.append(line)
                file.seek(0)
                file.truncate()
                file.writelines(updated_lines)
            print("Account information updated successfully.")
        except Exception and FileNotFoundError:
            print("User file not found or Errors. Please check your username.")
    def password_edit(self, username, old_password):
        try:
            main_file = username + ".User.txt"
            with open(main_file, 'r+') as file:
                lines = file.readlines()
                stored_password = lines[1].strip().split(": ")[1]
                if self.hash_password(old_password) != stored_password:
                    print("Password update failed. Incorrect old password.")
                    return
                new_password = input("Enter your new password: ")
                if not self.validate_password(new_password):
                    print("Invalid password format. Password update failed.")
                    return
                lines[1] = f"Password: {self.hash_password(new_password)}\n"
                file.seek(0)
                file.truncate()
                file.writelines(lines)
                print("Password updated successfully.")
        except FileNotFoundError:
            print("User file not found. Please check your username.")
        except Exception as e:
            print(f"Error during password update: {e}")