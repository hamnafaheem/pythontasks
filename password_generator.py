import random
import string

def generate_password(length, complexity):
    password = ''
    if 'uppercase' in complexity:
        password += random.choice(string.ascii_uppercase)
    if 'lowercase' in complexity:
        password += random.choice(string.ascii_lowercase)
    if 'digits' in complexity:
        password += random.choice(string.digits)
    if 'special' in complexity:
        password += random.choice(string.punctuation)

    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

def password_strength(password):
    strength = 0
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    return strength

def main():
    print("Welcome to the Password Generator!")

    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity of the password (e.g., uppercase, lowercase, digits, special): ").split()

    password = generate_password(length, complexity)
    print("Generated Password:", password)

    strength = password_strength(password)
    print("Password Strength:", strength, "out of 4")

if __name__ == "__main__":
    main()
