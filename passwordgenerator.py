import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8 characters
    length = max(length, 8)

    # Generate a random password using the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    # Prompt the user to specify the desired length of the password
    password_length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(password_length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
