class User:
    """A simple user class."""

    def __init__(self, first_name, last_name, location, age):
        """Initialize user class and attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """describes a user"""
        print(f"The user's name is {self.first_name} {self.last_name}.")
        print(f"The user is {self.age} years old and lives in {self.location}.")

    def greet_user(self):
        """Greets a user"""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increments number of login attempts by one"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets number of login attempts by one"""
        self.login_attempts = 0

user = User('John', 'Doe', 'Boston', 35)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts (after reset): {user.login_attempts}")
