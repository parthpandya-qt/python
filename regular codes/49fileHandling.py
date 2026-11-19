#this is used to write the file

# f=open("./parth.txt","r")
# text = f.read()
# print(text)
# f.close()


import os
print(os.getcwd())



f=open("parth.txt","a")
f.write("this is new file created")
f.close()



file_path = r"C:\Users\parth\OneDrive\Documents\Desktop\python\regular codes\parth.txt"
f=open(file_path,"a")
f.write("this is new file created by path pandya")
f.close()


file_path = r"C:\Users\parth\OneDrive\Documents\Desktop\python\regular codes\parth.txt"
f=open(file_path,"r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
