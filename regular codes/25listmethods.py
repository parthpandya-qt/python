list = [1,2,5,6,8,7,6,5,4,9,5,2,1]

list.append(45)
print(list)



list.sort()
print(list)

list.sort(reverse="True")     

print(list)

list.reverse()
print(list)

print(list.index(7))

print(list.count(1))

m= list.copy()
print(m)

list.insert(5,899)
print(list)


q=[50,60,40]
list.extend(q)
print(list)

k = list + q
print(k)

list[2]=0

print(list)