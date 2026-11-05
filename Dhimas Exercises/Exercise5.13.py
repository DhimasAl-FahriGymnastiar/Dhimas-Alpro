budget = 1000000
expenses = []

while True:
    print("\n=== PERSONAL EXPENSE TRACKER ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Check remaining budget")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Expense name: ")
        amount = int(input("Expense amount: "))
        expenses.append({
            'name': name,
            'amount': amount
        })
        print("Expense added successfully!")

    elif choice == '2':
        for expense in expenses:
            print(f"{expense['name']}: Rp{expense['amount']}")

    elif choice == '3':
        total = sum(expense['amount'] for expense in expenses)
        remaining = budget - total

        print(f"Total expenses: Rp{total}")
        print(f"Remaining budget: Rp{remaining}")

    elif choice == '4':
        print("Thank you for using the program!")
        break

    else:
        print("Invalid option!")