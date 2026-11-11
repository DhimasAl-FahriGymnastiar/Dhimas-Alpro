import random

possibilities = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

winning_ticket = random.sample(possibilities, 4)

my_ticket = [1, "A", 5, "C"]

attempts = 0

while True:
    pulled_ticket = random.sample(possibilities, 4)
    attempts += 1

    if set(pulled_ticket) == set(my_ticket):
        break

print("My ticket:", my_ticket)
print("Winning ticket:", pulled_ticket)
print(f"It took {attempts} attempts to win!")