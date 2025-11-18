while True:
    first_number = input("First number: ")
    if first_number.lower() == 'q':
        break

    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("you can only enter numbers\n")
    else:
        print(f"The sum is: {result}\n")