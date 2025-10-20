nick = {  'first_name': 'Nick', 'last_name': 'Graziano','age': '18', 'city': 'Freehold'}

jd = { 'first_name': 'JD', 'last_name': 'Graziano', 'age': '20', 'city': 'Freehold'}

eric = {'first_name': 'Eric','last_name': 'Lavin','age': '20','city': 'Freehold'}


people = [nick, jd, eric]


for person in people:
    print(f"\nName: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")