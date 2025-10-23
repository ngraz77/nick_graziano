def make_sandwich(*items):
    print("Making a sandwich with:")
    for item in items:
        print(f"- {item}")

make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "avocado")
make_sandwich("peanut butter", "jelly")