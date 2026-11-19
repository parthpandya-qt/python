class person:
    name="Parth Pandya"
    age = 19
    gender = "Male"
    occupation ="Data Scientist"  #object 
    def info(self):
        print(f"{self.name} is a {self.occupation}.")    #method

a=person()
print(a.name, a.age, a.gender)

a.info()


b=person()
b.name="Samyak Chattar"
b.age=19
b.gender="Male"

b.info()

print(b.name, b.age, b.gender)
a.info()