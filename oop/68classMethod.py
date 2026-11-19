class Employee:
    company="Apple"
    def show(self):
        print(f"This is a {self.name} and company is {self.company}")

    @classmethod
    def changecompany(cls,new_company):
        cls.company=new_company



e1=Employee()
e1.name="Parth"

e1.show()

e1.changecompany("Twitter")
e1.show()





# as a constructor

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first, last = full_name.split()
        return cls(first, last)

user = User.from_full_name("Ada Lovelace")