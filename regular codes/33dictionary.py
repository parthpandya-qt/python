dic ={
    "name":"parth",
    "class":12,
    "roll no":45,
    1717: "student id"
}

print(dic[1717])
print(dic["name"])
print(dic["class"])

print(dic.get("name"))

print(dic.keys())

for key in dic.keys():
    print(key)

print(dic.items())    

for key, value in dic.items():
    print(key, value)