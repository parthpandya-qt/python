# f= open("parth1.txt","w")
# f.write("Hi my name is Parth Pandya")

# f.truncate(10)

f= open("parth1.txt","r")
data=f.read()
print(data)

f.close()