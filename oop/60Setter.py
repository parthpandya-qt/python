class section_l:
    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
    # def fullname(self):
    #     print(f"Name of student is {self.firstName} and {self.lastName}")


    @property
    def fullname(self):
        return f"{self.firstName} {self.lastName}"

    @fullname.setter
    def fullname(self, first):
        self.firstName = first

student1 = section_l("John", "Doe")   #value stored 


student1.fullname = "Jane"  # setter method invok

print(student1.fullname ) # getter method invok again to verify the change