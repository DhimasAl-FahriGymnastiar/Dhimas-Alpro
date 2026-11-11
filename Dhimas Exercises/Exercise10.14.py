import json

def get_new_username():
    username = input("What is your name? ")

    with open("username.json", "w") as file:
        json.dump(username, file)

    return username

def greet_user():
    try:
        with open("username.json") as file:
            username = json.load(file)

    except FileNotFoundError:
        username = get_new_username()

    else:
        correct = input(
            f"Are you {username}? (yes/no): "
        )

        if correct.lower() != "yes":
            username = get_new_username()

    print(f"Welcome back, {username}!")

greet_user()