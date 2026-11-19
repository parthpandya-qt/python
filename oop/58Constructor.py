class details:
    def __init__(self,a,b):
        self.name = a
        self.age = b
    def info(self):
        print(f"{self.name} age is {self.age}")


a=details("Parth",19)   
a.info()     

b=details("Rohan",20)

b.info()