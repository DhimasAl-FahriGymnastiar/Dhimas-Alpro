class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Vanilla", "Strawberry", "Matcha"]

    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream = IceCreamStand("Sweet Ice Cream", "Dessert")

ice_cream.describe_restaurant()
ice_cream.display_flavors()