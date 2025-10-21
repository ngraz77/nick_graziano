cities = {'new york': {'country': 'usa','population': '8 million','fact': 'known for great pizza'},'tokyo': {'country': 'japan','population': '14 million','fact': 'world’s most populous metropolitan area'},'paris': {'country': 'france','population': '2 million','fact': 'home to the famous eiffel tower'}}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact'].capitalize()}")