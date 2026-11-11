#cats.txt
#Kitty
#Luna
#Milo

#dogs.txt
#Buddy
#Max
#Charlie

#Main
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents)

    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")