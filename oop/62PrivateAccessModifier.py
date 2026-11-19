class Employee:
    def __init__(self):
        self.__name = "Parth"

a=Employee()

# print(a.name)  # error dega

print(a._Employee__name)    #name mangling

print(a.__dir__())  # show all attributes and methods of class