# f= open("parth.txt","r")

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line) 

f= open("marks.txt","r")

i=0

while True:
    i=i+1
    line = f.readline()
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]

    print(f"marks of student{i} in math is {m1}")
    print(f"marks of student{i} in science is {m2}")
    print(f"marks of student{i} in sst is {m3}")
    if not line:
        break
    print(line)
   