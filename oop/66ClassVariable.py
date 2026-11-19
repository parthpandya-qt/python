class employee:
    company="Apple"   #class variable
    noofEmployee=0
    def __init__(self, name):
        self.name = name
        employee.noofEmployee += 1  #incrementing the class variable

    def info(self):
        print(f"{self.name} {self.noofEmployee} {self.company}")


a=employee("parth")       
b=employee("Krish")       
c=employee("Samyak")       
d=employee("Yash")       
e=employee("Rupabh")       
f=employee("Tejas")       
g=employee("Ojas")       
   
a.info() 
