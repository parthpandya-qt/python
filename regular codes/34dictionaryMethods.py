s={
    1:90,
    2:85,
    3:95,
    4:85,
    5:92
}

p={
    10:90,
    20:85,
    30:95,
    40:85,
    50:92
}

s.update(p)
print(s) 

# s.clear() # clear the dictionary
s.pop(4) # remove the key 4

print(s)

s.popitem() # remove the last key value pair
print(s)

del s[1] # remove the key 1
print(s)