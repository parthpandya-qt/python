class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):      # Dog inherits from Animal
    def sound(self):
        print("Dog barks.")

class Cat(Animal):      # Cat inherits from Animal
    def sound(self):
        print("Cat meows.")

class Cow(Animal):      # Cow inherits from Animal
    def sound(self):
        print("Cow moos.")

# Create objects of each child class
d = Dog()
c = Cat()
w = Cow()

# Call their respective sound methods
d.sound()   # Dog-specific
c.sound()   # Cat-specific
w.sound()   # Cow-specific
