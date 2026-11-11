filename = "book.txt"

try:
    with open(filename, encoding="utf-8") as file:
        contents = file.read()

    word_the = contents.lower().count("the")
    word_the_space = contents.lower().count("the ")

    print(f"Total word 'the': {word_the}")
    print(f"Total word 'the ' (with space): {word_the_space}")

except FileNotFoundError:
    print("The file was not found.")