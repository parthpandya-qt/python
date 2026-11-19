
class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
    
    def __str__(self):
        return f"{self.make} ({self.year})"  # User-friendly
    
    def __repr__(self):
        return f"Car(make='{self.make}', year={self.year})"  # Developer-friendly

car = Car("Tesla", 2023)
print(str(car))   # Tesla (2023)      → uses __str__
print(car)        # Tesla (2023)      → also uses __str__
print(repr(car))  # Car(make='Tesla', year=2023) → uses __repr__
