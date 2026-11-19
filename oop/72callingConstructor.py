class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class programmer(employee):
    def __init__(self,name,age,lang):
        super().__init__(name, age)
        self.lang = lang


p=programmer("Parth",19,"python")
print (p.name)
print (p.age)
