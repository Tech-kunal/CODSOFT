import random
import string

def generate_password(length) -> str:
    all_characters = string.ascii_letters + string.digits + string.punctuation

    if length < 8:
        print("Password must be at least 8 characters")
        return None

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("What length would you like your password to be: "))
    password = generate_password(length)

    if password:
        print("Random password for the user:", password)

if __name__ == "__main__":
    main()
