class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


my_car = ElectricCar("Tesla", "Model S", 2024)

my_car.describe_car()

print("Before battery upgrade:")
my_car.battery.get_range()

my_car.battery.upgrade_battery()

print("After battery upgrade:")
my_car.battery.get_range()