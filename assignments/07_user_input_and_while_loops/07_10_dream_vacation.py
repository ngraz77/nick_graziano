responses = {}

# Flag to control the polling loop
polling_active = True



while polling_active:
    name = input("What is your name? ")
    if name.lower() == 'quit':
        break
    
    destination = input("If you could visit one place in the world, where would you go? ")
    if destination.lower() == 'quit':
        break
    
    responses[name] = destination
    print(f"Thank you, {name.title()}! Your response has been recorded.\n")

print("\n--- Dream Vacation Poll Results ---")
for name, destination in responses.items():
    print(f"{name.title()} would like to visit {destination.title()}.")