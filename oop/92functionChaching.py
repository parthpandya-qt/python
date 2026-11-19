import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * n



print(fx(2))  
print("print will act after 5 seconds")

print(fx(5))  
print("print will act after 5 seconds")


print(fx(7))
print("print will act after 5 seconds")


print(fx(3))  
print("print will act after 5 seconds")


print(fx(2))  
print("print will not act after 5 seconds")

print(fx(5))  
print("print will not act after 5 seconds")



import functools
print(dir(functools))  # to see all the methods of functools module