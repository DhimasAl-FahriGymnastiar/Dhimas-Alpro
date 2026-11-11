try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 + number2

    print(f"The result is: {result}")

except ValueError:
    print("Please enter valid numbers!")