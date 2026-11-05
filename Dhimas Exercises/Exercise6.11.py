cities = {
    'Surakarta': {
        'country': 'Indonesia',
        'population': 500000,
        'fact': 'Known as Solo.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 14000000,
        'fact': 'Has an extensive train system.'
    },
    'Paris': {
        'country': 'France',
        'population': 2100000,
        'fact': 'Home of the Eiffel Tower.'
    }
}

for city, information in cities.items():
    print(f"\n{city}:")
    for key, value in information.items():
        print(f"{key.title()}: {value}")