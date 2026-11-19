double = lambda x:x*2


print(double(5))


avg = lambda x,y:(x+y)/2

print(avg(5,4))



def appl(avg,x):
    return 10+avg(x)

print(appl(lambda x:x*x*x,2))


