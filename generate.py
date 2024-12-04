import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''.join([
        string.ascii_uppercase if use_uppercase else '',
        string.ascii_lowercase if use_lowercase else '',
        string.digits if use_digits else '',
        string.punctuation if use_special else ''
    ])
    
    if not characters:
        raise ValueError("Please select at least one type of character.")

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_uppercase = input("Use uppercase letters? (y/n): ") == 'y'
    use_lowercase = input("Use lowercase letters? (y/n): ") == 'y'
    use_digits = input("Use digits? (y/n): ") == 'y'
    use_special = input("Use special characters? (y/n): ") == 'y'

    while True:
        try:
            print(f"Generated password: {generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)}")
        except ValueError as e:
            print(e)
            break
        input("Press Enter to generate a new password...")
