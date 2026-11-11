#favorite_numbers.py
import json
number = input("What is your favorite number? ")

with open("favorite_number.json", "w") as file:
    json.dump(number, file)

print("Your favorite number has been saved!")

#read_favorite_number.py
import json

with open("favorite_number.json") as file:
    number = json.load(file)

print(f"I know your favorite number! It's {number}.")