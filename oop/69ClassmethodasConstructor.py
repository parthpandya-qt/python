class employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    
    @classmethod
    def from_string(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    def info(self):
        print(f"Employee name: {self.name}, Salary: {self.salary}")


    

string="Parth-3200000"
e1=employee.from_string(string)
e1.info()

