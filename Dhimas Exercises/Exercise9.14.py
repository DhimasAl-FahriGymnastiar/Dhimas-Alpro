import random

possibilities = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

winning_ticket = random.sample(possibilities, 4)

print("Any ticket matching these numbers or letters wins a prize!")
print("Winning ticket:", winning_ticket)