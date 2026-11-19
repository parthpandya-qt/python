class person:
        def __init__(self,name,age,occupation):
            self.name = name
            self._age = age
            self.__occupation = occupation



person1 = person("Parth Pandya", 19, "Data Scientist")

print(person1.name)
print(person1._age)
print(person1._person__occupation)      #name mangling is used to access private variable