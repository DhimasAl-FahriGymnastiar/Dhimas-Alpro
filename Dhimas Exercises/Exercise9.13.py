from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

# 6-sided die
print("Rolling 6-sided die:")
die6 = Die()

for i in range(10):
    die6.roll_die()

# 10-sided die
print("\nRolling 10-sided die:")
die10 = Die(10)

for i in range(10):
    die10.roll_die()

# 20-sided die
print("\nRolling 20-sided die:")
die20 = Die(20)

for i in range(10):
    die20.roll_die()