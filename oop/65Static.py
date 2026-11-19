class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        return self.num + n

    @staticmethod
    def add(a,b):
        return a + b    
    

a=math(5)

print(a.addtonum(6))
print(a.num)
print(a.add(44 ,800))

print(math.add(5,800))
