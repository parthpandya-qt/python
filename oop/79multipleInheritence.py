class Son:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def info(self):
        print(f"{self.firstName} {self.lastName}")

class Family:
    def __init__(self, Father, Mother):
        self.Father = Father
        self.Mother = Mother
         
    def info(self):
        print(f"Father: {self.Father.firstName} {self.Father.lastName}")
        print(f"Mother: {self.Mother.firstName} {self.Mother.lastName}")

class Occupation(Family, Son):
    def __init__(self, firstName, lastName, Father, Mother, occupation):
        Son.__init__(self, firstName, lastName)
        Family.__init__(self, Father, Mother)
        self.occupation = occupation        

    def info(self):
        print(f"Son: {self.firstName} {self.lastName}")
        print(f"Occupation: {self.occupation}")
        print(f"Father: {self.Father.firstName} {self.Father.lastName}")
        print(f"Mother: {self.Mother.firstName} {self.Mother.lastName}")

# Create Father and Mother as Son instances (to have firstName and lastName attributes)
father = Son("Vijay", "Pandya")
mother = Son("Sapna", "Pandya")

# Create Occupation instance
A = Occupation("Parth", "Pandya", father, mother, "Data Scientist")

A.info()





class Camera:
    def take_photo(self):
        print("Taking a photo")

class Phone:
    def make_call(self):
        print("Making a call")

class SmartPhone(Camera, Phone):
    pass

phone = SmartPhone()
phone.take_photo()
phone.make_call()

print(SmartPhone.mro())