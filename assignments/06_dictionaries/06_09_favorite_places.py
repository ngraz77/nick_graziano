favorite_places = {'Nick': ['New York'],'JD': ['Home'],'Eric': ['New Jersey']}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite place(s):")
    for place in places:
        print(f"- {place}")