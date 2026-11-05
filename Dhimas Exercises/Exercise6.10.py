favorite_numbers = {
    'Budi': [7, 10],
    'Andi': [3, 8],
    'Siti': [5, 12],
    'Rina': [2, 9],
    'Doni': [4, 11]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers:")
    for number in numbers:
        print(number)