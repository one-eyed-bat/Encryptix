import random
import string

strength = int(input("Choose password strength. 1=weak, 10=strong"))

def generate_password(strength):
    characters = string.ascii_letters + string.digits + string.punctuation

    if 1 <= strength <= 3:
        length = 8
        choice = string.ascii_letters

    elif 4 <= strength <= 7:
        length = 12
        choice = string.ascii_letters + string.digits

    elif 7 <= strength <= 10:
        choice = characters
        length = 16

    else:
        print("please choose a number between 1, and 10")
    password = ''.join(random.choice(choice) for _ in range(length))

    print(password)

generate_password(strength)

