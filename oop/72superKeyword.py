class superClass:
    def parentMethod(self):
        print("this is super class")

class childClass(superClass):
    def childMethod(self):
        print("this is child class")
        super().parentMethod()
    def parentMethod(self):
        print("this is overridden method")    
        
p=childClass()
p.childMethod()

p.parentMethod()  # this will call overridden method from child class