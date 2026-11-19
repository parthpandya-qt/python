def filter_function(x):
    return x > 4

v=[12,4,6,7,2,3]
# ls=[]
# for i in v:
#    if(i>4):
#       ls.append(i)
# print(ls)

x=list(filter(filter_function,v))

print(x)