class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def make_sound(self):
        return "Some generic sound"
    
class Dog(Animal):
    def __init__(self, species,name, breed):
        # Correct call: self must be passed explicitly
        Animal.__init__(self,species, name)
        self.breed = breed

    def make_sound(self):
        return "Woof Woof"

# Create Dog instance
a = Dog("dog","Buddy", "German Shepherd")

# Access attributes
print(a.species)  # dog
print(a.name)     # Buddy
print(a.breed)    # German Shepherd

# Test method override
print(a.make_sound())  # Woof Woof
