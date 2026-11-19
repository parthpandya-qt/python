def cube(x):
    return x**3

v=[12,4,6,7,2,3]
# ls=[]
# for i in list :
#     ls.append(cube(i))
    
# print(ls)

p = list(map(cube, v))

print(p)


