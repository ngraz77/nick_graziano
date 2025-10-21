print("Enter pizza toppings one at a time.")
print("Type 'quit' when you are finished.\n")

while True:
    topping = input("Enter a topping: ")

    if topping.lower() == 'quit':
        print("Your pizza will be ready soon!")
        break
    else:
        print(f"I'll add {topping.title()} to your pizza.")