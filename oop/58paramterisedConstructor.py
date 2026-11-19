class details:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"{self.name} age is {self.age}")


a=details("Parth",19)   
a.info()     

b=details("Rohan",20)

b.info()