import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    lowercase_letters = string.ascii_lowercase if use_lowercase else ''
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special else ''
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if not all_characters:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        try:
            password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
            print(f"Generated Password: {password}")
        except ValueError as e:
            print(e)

        another = input("Do you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

    print("Thank you ")

if __name__ == "__main__":
    main()