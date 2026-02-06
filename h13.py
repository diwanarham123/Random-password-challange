import random
import string

def generate_random_password(length=12):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits

    all_chars = lowercase_chars + uppercase_chars + digit_chars

    password = [
        random.choice(lowercase_chars),
        random.choice(uppercase_chars),
        random.choice(digit_chars)
    ]

    if length < 3:
        length = 3
        print("Password length too short, setting to minimum length of 3.")

    for _ in range(length - 3):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password)


print("Welcome to the Password Generator Game!")

while True:
    try:
        user_input_length = input("Enter desired password length (or 'q' to quit): ")
        if user_input_length.lower() == 'q':
            print("Thanks for playing!")
            break

        length = int(user_input_length)
        if length <= 0:
            print("Please enter a positive number for length.")
            continue

        generated_password = generate_random_password(length)
        print(f"Your new password: {generated_password}")
        print("----------------------------------------")

    except ValueError:
        print("Invalid input. Please enter a number or 'q'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
