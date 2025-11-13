class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = (1, self.sides)
        print(number)

die6 = Die()
print("Roll a 6-sided die:")
for _ in range(10):
    print(die6.roll_die())

die10 = Die(10)
print("\nRoll a 10-sided die:")
for _ in range(10):
    print(die10.roll_die())

die20 = Die(20)
print("\nRoll a 20-sided die:")
for _ in range(10):
    print(die20.roll_die())