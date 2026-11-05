person1 = {
    'first_name': 'Budi',
    'last_name': 'Santoso',
    'age': 20,
    'city': 'Surakarta'
}

person2 = {
    'first_name': 'Andi',
    'last_name': 'Wijaya',
    'age': 21,
    'city': 'Jakarta'
}

person3 = {
    'first_name': 'Siti',
    'last_name': 'Aminah',
    'age': 19,
    'city': 'Yogyakarta'
}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")
    print()