class employee:
    def __init__(self, name):
        self.name = name
        self.raise_income = .02

    def info(self):
        print(f"{self.name} {self.raise_income}")


a=employee("parth")       
a.info() 