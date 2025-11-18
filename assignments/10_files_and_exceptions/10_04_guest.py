name = input("What is your name? ")

with open('guest.txt', 'w') as file_object:
    file_object.write(name)

print("Your name has been written to guest.txt.")