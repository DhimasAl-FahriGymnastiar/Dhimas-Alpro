class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant("Warung Pak Budi", "Indonesian Food")

# Print initial number of customers
print("Initial customers:", restaurant.number_served)

# Change the number of customers
restaurant.number_served = 10
print("Updated customers:", restaurant.number_served)

# Set a new number of customers
restaurant.set_number_served(50)
print("After set_number_served:", restaurant.number_served)

# Increment the number of customers
restaurant.increment_number_served(25)
print("After increment_number_served:", restaurant.number_served)