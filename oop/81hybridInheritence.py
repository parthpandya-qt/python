class Person:
    def info(self):
        print("Person: Basic details.")

class Employee(Person):  # Single inheritance from Person
    def info(self):
        print("Employee: Working in a company.")
        super().info()  # Calls Person's info

class Student(Person):   # Another single inheritance from Person
    def info(self):
        print("Student: Studying at college.")
        super().info()  # Calls Person's info

class Intern(Employee, Student):  # Multiple inheritance: combines Employee and Student
    def info(self):
        print("Intern: Learning and working as intern.")
        super().info()  # Follows MRO: calls Employee.info()

# Create object of Intern
intern = Intern()
intern.info()

# Display Method Resolution Order
print("\nMRO of Intern class:")
for cls in Intern.mro():
    print(cls)
