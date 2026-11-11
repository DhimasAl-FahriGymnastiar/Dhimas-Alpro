while True:
    print("\nEnter two numbers to add.")
    print("Enter 'q' to quit.")

    number1 = input("First number: ")

    if number1 == "q":
        break

    number2 = input("Second number: ")

    if number2 == "q":
        break

    try:
        result = int(number1) + int(number2)
        print(f"The result is: {result}")

    except ValueError:
        print("Please enter valid numbers!")