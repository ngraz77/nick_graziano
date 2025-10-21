print("Welcome to the movie theater!")
print("Enter 'quit' at any time to stop.\n")

while True:
    age_input = input("Please enter your age: ")

    if age_input.lower() == 'quit':
        print("Thank you for visiting! Enjoy your movie!")
        break

    age = int(age_input)

    if age < 3:
        print("Your ticket is free!\n")
    elif age <= 12:
        print("Your ticket costs $10.\n")
    else:
        print("Your ticket costs $15.\n")