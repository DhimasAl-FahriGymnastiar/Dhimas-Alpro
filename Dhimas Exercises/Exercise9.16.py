import random

numbers = [1, 2, 3, 4, 5]

print(random.random())
print(random.randint(1, 10))
print(random.choice(numbers))
print(random.sample(numbers, 3))

random.shuffle(numbers)
print(numbers)