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

class Admin(User):
    """A simple admin class."""

    def __init__(self, first_name, last_name, location, age, privileges):
        """Initialize admin class and attributes."""
        self.first_name = first_name
        self.last_name =last_name
        self.location = location
        self.age = age
        self.privileges = privileges

    def show_privileges(self):
        """Display privileges"""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin_1 = Admin('Adam', 'Admin', 'NYC', 26, ['can add post', 'can delete post', 'can ban user'])
admin_1.show_privileges
