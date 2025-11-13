from lottery import Lottery

my_ticket = ['1', 'b', '7', 'd']

attempts = 0
won = False

while not won:
    attempts += 1
    winning_ticket = (Lottery, 4)
    if sorted(winning_ticket) == sorted(my_ticket):
        won = True

print(f"\nYour ticket {my_ticket} won after {attempts} attempts")