pet1 = {'animal': 'cat', 'owner': 'Budi'}
pet2 = {'animal': 'dog', 'owner': 'Andi'}
pet3 = {'animal': 'rabbit', 'owner': 'Siti'}

pets = [pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
    print()