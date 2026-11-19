mixed=[5,8,5,True,"parth","pandya"]

print(mixed)
print(mixed[0])
print(len(mixed))

print(mixed[-3])   #length of list - 3


for i in mixed:
    if i == "parth":
        print("Yes")
        print(i)
        break
    else:
        print("No")
        print(i)


if "parth" in mixed:
    print("Yes")
else:
    print("No")


print(mixed[0:5:2])        #jump index