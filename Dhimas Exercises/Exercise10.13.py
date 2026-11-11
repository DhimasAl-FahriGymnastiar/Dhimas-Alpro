import json

filename = "user_info.json"

user_info = {}

user_info["username"] = input("Enter your username: ")
user_info["age"] = input("Enter your age: ")
user_info["city"] = input("Enter your city: ")

with open(filename, "w") as file:
    json.dump(user_info, file)

with open(filename) as file:
    saved_info = json.load(file)

print("\nHere's what I remember about you:")
print(f"Username: {saved_info['username']}")
print(f"Age: {saved_info['age']}")
print(f"City: {saved_info['city']}")