sandwich_orders = ['tuna', 'pastrami', 'turkey', 'ham', 'pastrami', 'veggie', 'chicken', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")