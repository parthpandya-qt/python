class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"[Vehicle] Created Vehicle: {self.brand} {self.model}")

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):  # Inherits from Vehicle
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
        print(f"[Car] Added doors: {self.doors}")

    def car_info(self):
        print(f"{self.brand} {self.model} has {self.doors} doors.")

class ElectricCar(Car):  # Inherits from Car, which inherits from Vehicle
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model, doors)
        self.battery_capacity = battery_capacity
        print(f"[ElectricCar] Battery capacity: {self.battery_capacity} kWh")

    def full_info(self):
        self.display()              # From Vehicle
        self.car_info()             # From Car
        print(f"Battery: {self.battery_capacity} kWh")  # From ElectricCar
   

my_tesla = ElectricCar("Tesla", "Model S", 4, 100)

print("\n--- Full Information ---")
my_tesla.full_info()   
