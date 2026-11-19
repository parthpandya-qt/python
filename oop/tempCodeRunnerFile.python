class Name:
    def __init__(self, firstName, lastName,):
        self.firstName = firstName
        self.lastName = lastName
        

    def info(self):
        print(f"{self.firstName} {self.lastName} ")

class family():
    def __init__(self,Father, Mother):
        self.Father = Father
        self.Mother = Mother
         
    def info(self):
        print(f"Father: {self.Father.firstName} {self.Father.lastName}")  
class Occupation(family, Name):
    def __init__(self, firstName, lastName, Father, Mother, occupation):
        Name.__init__(self, firstName, lastName)
        family.__init__(self, Father, Mother)
        self.occupation = occupation 
    def info(self):
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Father: {self.Father.firstName} {self.Father.lastName}")
        print(f"Mother: {self.Mother.firstName} {self.Mother.lastName}")
        print(f"Occupation: {self.occupation}")           

A=Occupation("Parth", "Pandya",Name("Vijay","Pandya"),Name("Sapna","Pandya"),"Data Scientist")  


A.info()

print(Occupation.__mro__)