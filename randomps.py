import random
import string

def generate_password(length, uppercase=True, digits=True, special_characters=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get user preferences for password complexity
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    special_characters = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Generate and display the password
    password = generate_password(length, uppercase, digits, special_characters)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
