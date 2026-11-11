#learning_python.txt
#In Python you can create variables to store data.
#In Python you can use loops to repeat tasks.
#In Python you can create functions to organize code.
#In Python you can use classes to create objects.
#In Python you can read and write files.

#Main
# Read the entire file
with open("learning_python.txt") as file:
    contents = file.read()

print(contents)

# Read the file line by line using a list
with open("learning_python.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())