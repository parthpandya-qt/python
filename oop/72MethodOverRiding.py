class superClass:
    def superMethod(self):
        print("This is from superclass")

class childClass(superClass):
    def superMethod(self):
        print("This is not from subclass")

a=childClass()

a.superMethod()    # This will print "This is from subclass" as it overrides the superclass method.
