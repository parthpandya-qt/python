from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):          # normal methods are fine too
        return f"Area is {self.area()}"

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2

class Broken(Shape):
    pass                          # forgot to implement area()

c = Circle(2)
print(c.describe())               # Area is 12.56636

Shape()                           # TypeError: Can't instantiate abstract class
Broken()                          # TypeError: same error, area() not implemented