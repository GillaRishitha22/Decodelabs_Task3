import random
import string

def generate_strong_password(length):
    if length < 4:
        return "Password length must be at least 4."

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = ''.join(
        random.choice(
            string.ascii_letters +
            string.digits +
            string.punctuation
        )
        for _ in range(length - 4)
    )

    password_list = list(
        lowercase + uppercase + digit + special + remaining
    )

    random.shuffle(password_list)

    return ''.join(password_list)

# Main Program
length = int(input("Enter password length: "))
password = generate_strong_password(length)

print("Generated Password:", password)