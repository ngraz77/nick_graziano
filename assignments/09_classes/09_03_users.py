class User:
    """A simple user class."""

    def __init__(self, first_name, last_name, location, age):
        """Initialize user class and attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age

    def describe_user(self):
        """describes a user"""
        print(f"The user's name is {self.first_name} {self.last_name}.")
        print(f"The user is {self.age} years old and lives in {self.location}.")

    def greet_user(self):
        """Greets a user"""
        print(f"Hello, {self.first_name} {self.last_name}!")

user_1 = User('Bob', 'the Builder', 'London', '42')
user_1.describe_user()
user_1.greet_user()

print("----")

user_2 =User('Peter','Parker', 'New York', '23')
user_2.describe_user()
user_2.greet_user()

