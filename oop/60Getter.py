class section_l:
    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
    def fullname(self):
        print(f"Name of student is {self.firstName} {self.lastName}")


    @property
    def fullName(self):
        print( f"{self.firstName} {self.lastName}")

student1 = section_l("John", "Doe")   #value stored 

student1.fullName  # getter method invoked


# class person:
#     def __init__(self,name,age,occupation):
#         self.name = name
#         self.age = age
#         self.occupation = occupation
#     def info(self):
#         print(f"{self.name} is a {self.occupation} and is {self.age} years old.")    

#     @property
#     def ageAftertenYears(self):
#         print(self.age + 10)
    
    
    
#     @ageAftertenYears.setter
#     def ageAftertenYears(self, value):
#         self.age = value - 10
#         print(f"Age after 10 years will be {self.age + 10} years old.")    

# a=person("Parth Pandya", 19, "Data Scientist")
# a.info()
# a.ageAftertenYears
# a.ageAftertenYears = 30  # setter method invoked