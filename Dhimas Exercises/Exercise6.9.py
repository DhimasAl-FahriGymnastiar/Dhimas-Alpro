favorite_places = {
    'Budi': ['Bali', 'Yogyakarta'],
    'Andi': ['Japan', 'Singapore'],
    'Siti': ['Paris', 'London', 'Seoul']
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places:")
    for place in places:
        print(f"- {place}")