class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def info(self):
        print(f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}")

a=Employee("Parth Pandya ",1717,1000)
a.info()

class newEmployee(Employee):
    def language(self):
        print(f"{self.name} speaks English and Hindi.")


b = newEmployee("samyak ",1715,1000)

b.info()
b.language()