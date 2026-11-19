def my_generator():
    for i in range(1, 100):
        yield i * i 

P=my_generator()
# for i in range(10):
#     print(next(P))

print(next(P))        
print(next(P))        
print(next(P))        
print(next(P))        
print(next(P))        


# A generator is a kind of iterator that gives you values one at a time, as they’re needed. It doesn’t build and store the entire sequence in memory first

def list_items(items):
    for item in items:
        yield item

fruits = ["apple", "banana", "cherry"]

for fruit in list_items(fruits):
    print(fruit)