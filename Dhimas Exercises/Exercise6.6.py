favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people = ['jen', 'sarah', 'mike', 'john', 'phil']

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding.")
    else:
        print(f"{person.title()}, please take the poll.")