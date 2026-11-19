def greet(fx):
    def name():
        print("Parth Pandya")
        fx()
        print("Hello, World!")
    return name

@greet
def hello():              #def hello():
    print("This is a decorator example.")     # print("This is a decorator example.")
    #hello = greet(hello)

hello()

def announce(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")
    return wrapper

@announce
def greet():
    print("Hello!")

greet()