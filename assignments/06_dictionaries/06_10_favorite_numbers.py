favorite_numbers = {'Nick': [21, 7],'JD': [7, 14, 28],'AJ': [35, 12],'Eric': [10, 5],'Matt': [23, 9, 45]}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")