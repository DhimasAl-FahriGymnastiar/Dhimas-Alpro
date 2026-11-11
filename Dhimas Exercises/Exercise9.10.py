class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
        
#Main program
from restaurant import Restaurant

my_restaurant = Restaurant("Warung Pak Budi", "Indonesian Food")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()