import json

filename = "favorite_number.json"

try:
    with open(filename) as file:
        number = json.load(file)

except FileNotFoundError:
    number = input("What is your favorite number? ")

    with open(filename, "w") as file:
        json.dump(number, file)

    print("Your favorite number has been saved!")

else:
    print(f"I know your favorite number! It's {number}.")