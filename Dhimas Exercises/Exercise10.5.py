print("Enter 'quit' to exit.")

while True:
    name = input("What is your name? ")

    if name == "quit":
        break

    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")

    print(f"Hello, {name}! You have been added to the guest book.")