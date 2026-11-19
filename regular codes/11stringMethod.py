p = "!!!Parth Pandya   !!!!!!"

print(p.lower())

print(p.upper())

print(p.rstrip("!"))   #remove right side space !!!!!!!

print(p.replace("Parth","advik")) #replace Parth with advik

print(p.split(" "))   #split the string into list of words

print(p.capitalize())

print(p.center(50))

print(p.count("P"))  #count the number of P in string

print(p.endswith("!!!"))

print(p.endswith("an",4,6))

print(p.find("an")) # returns the index of pa at first occurence

print(p.index("an"))  #similar to find par ye error return kar dega agap input nahi mila to

print(p.isalnum())  #return true if string contain lpha numeri

print(p.isalpha())  #return true if string contain A-Z and a-z characters

print(p.isprintable())  #return if the string is printable


x="Parth Pandya"
print(x.istitle()) # return if the first character of string is uppercase 

print(x.swapcase()) #swap the case of string

print(x.title())  #convert the first letter of each word to uppercase



