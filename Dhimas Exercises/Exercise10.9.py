filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents)

    except FileNotFoundError:
        pass