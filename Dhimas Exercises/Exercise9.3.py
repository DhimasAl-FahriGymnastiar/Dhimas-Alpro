class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

user1 = User("Andi", "Pratama", 20, "andi@gmail.com", "Solo")
user2 = User("Budi", "Santoso", 21, "budi@gmail.com", "Jakarta")
user3 = User("Citra", "Lestari", 19, "citra@gmail.com", "Bandung")

user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()