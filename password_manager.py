import json
import random
import string

# Function to load passwords from a JSON file
def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save passwords to a JSON file
def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=4)

# Function to generate a complex password
def generate_password(length=12):
    # Define character sets for each category
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure that at least one character from each category is included
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the remaining password length with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the password to make it more secure
    random.shuffle(password)

    # Convert the list of characters to a string
    return ''.join(password)

# Function to create a new password
def create_password():
    print("Generating a complex password:")
    # Generate a complex password
    password = generate_password()
    print(f"Generated Password: {password}")
    print("You can copy and save this password.")
    return password

# Function to add a new password
def add_password():
    name = input("Enter the name of the service or website: ")
    username = input("Enter your username: ")
    choice = input("Do you want to generate a password? (yes/no): ").lower()
    if choice == 'yes':
        password = create_password()
    else:
        password = input("Enter your own password: ")

    passwords = load_passwords()
    passwords[name] = {'username': username, 'password': password}
    save_passwords(passwords)
    print("Password saved successfully!")

# Function to retrieve a password
def get_password():
    name = input("Enter the name of the service or website: ")
    passwords = load_passwords()
    if name in passwords:
        username = passwords[name]['username']
        password = passwords[name]['password']
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print("Password not found.")

# Main menu loop
while True:
    print("\nPassword Manager Menu:")
    print("1. Generate Password")
    print("2. Add Password")
    print("3. Get Password")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == '1':
        create_password()
    elif choice == '2':
        add_password()
    elif choice == '3':
        get_password()
    elif choice == '4':
        print("Exiting Password Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")