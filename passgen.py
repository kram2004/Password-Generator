import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the length is at least 4, with at least one character from each set
    if length < 4:
        print("Password length should be at least 4.")
        return

    # Ensure a minimum length of 8 characters
    if length < 8:
        print("Warning: It is recommended to use a password length of at least 8 characters.")

    # Choose at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the remaining length with random characters
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to randomize the order of characters
    random.shuffle(password)

    # Convert the list of characters to a string
    password_str = ''.join(password)

    return password_str

if __name__ == "__main__":
    # Take password length as input from the user
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    generated_password = generate_password(password_length)

    print(f"Generated Password: {generated_password}")
