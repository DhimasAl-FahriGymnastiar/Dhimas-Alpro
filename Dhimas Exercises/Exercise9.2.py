class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")

restaurant1 = Restaurant("Warung Padang", "Padang Food")
restaurant2 = Restaurant("Pizza Hut", "Italian Food")
restaurant3 = Restaurant("Sushi Hiro", "Japanese Food")

restaurant1.describe_restaurant()
print()

restaurant2.describe_restaurant()
print()

restaurant3.describe_restaurant()