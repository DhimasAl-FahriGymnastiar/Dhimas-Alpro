class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Andi", "Pratama", 20, "andi@gmail.com")

admin.describe_user()
admin.show_privileges()