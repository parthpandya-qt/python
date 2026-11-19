s1={4,5,6,4,7,8,88,11,100}
s2={6,4,7,54}

print(s1.union(s2))  # tu find the union of two set

print(s1.intersection(s2))  # to find the common elements between two set

#s1.update(s2) # update the set s1 with the elements of set s2
#print(s1)

#s1.intersection_update(s2) # update the set s1 with the elements of set s2
#print(s1)

s3 = s1.symmetric_difference(s2)  
print(s3)

s4 = s1.difference(s2)
print(s4)

print(s1.isdisjoint(s3)) # disjoint intersection

print(s1.issubset(s2)) # check if set s1 is subset of set s2(s1.isup(s2)) # check if set s1 is subset of set s2

print(s1.issuperset(s2)) # check if set s1 is superset of set s2

s1.add(1000)  # add an element to the set
print(s1)

s1.remove(1000)  # if the element is not present in the set then it will give an error
print(s1)

s1.discard(1000)  # if the element is not present in the set then it will not give any error
print(s1)    

item = s1.pop()  # remove the element from the set
print(s1)
print(item)



p={4,5,6,4,7,8,8,8}
del p

q={4,7,55,6,3}
q.clear()
print(q)