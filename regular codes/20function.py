def geometricMean(a,b):
    mean = (a*b)/(a+b)
    return mean

print(geometricMean(2, 4)) # Expected output: 1.333

def greaterThan(a,b):
    if a>b:
         print("a is greater")
    else:
         print("b is greater")

greaterThan(2, 4) # Expected output: b is greater
