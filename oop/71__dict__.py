class employees:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary


P=employees("parth",19,"IT",3200000)



a = P.__dict__  # make a dictionary of the object

for key, value in a.items():
    print(f"{key} : {value}")