# Task 3 - Password Generator
import random
import string

def generate_password():
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password should be at least 4 characters.")
            return
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

generate_password()
