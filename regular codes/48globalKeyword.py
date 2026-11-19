x=5


def hello():
    global x
    x=6
    print("This x is local variable :",x)

    y=56
    print("This y is local variable :",y)


hello()
print("This X is global variable :" ,x)   