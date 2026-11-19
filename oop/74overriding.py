class grandFather:
    def __init__(self):
        print("grandfather constructor called")

    def myMethod(self):
        print("grandfather method called")
class father(grandFather):
    def __init__(self):
        print("father constructor called")
        super().__init__()  # calling the constructor of grandFather class

    def myMethod(self):
        print("father method called")
        super().myMethod()  # calling the method of grandFather class

a=father()  # this will call the constructor of father class and then grandfather class constructor
a.myMethod()  # this will call the method of father class and then grandfather class method

b=grandFather()  # this will call the constructor of grandfather class
b.myMethod