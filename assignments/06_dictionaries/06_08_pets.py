pet1 = { 'animal_type': 'dog','owner': 'nick'}

pet2 = { 'animal_type': 'cat', 'owner': 'jd'}

pet3 = {'animal_type': 'hamster','owner': 'eric'}

pet4 = { 'animal_type': 'parrot', 'owner': 'laura'}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print("\nHere is what I know about this pet:")
    print(f"Animal type: {pet['animal_type'].title()}")
    print(f"Owner: {pet['owner'].title()}")