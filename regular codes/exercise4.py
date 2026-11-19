import string
import random
import math
x = input("Enter wheather you wants to Encrypt or Decrypt: ").strip().lower()



lowercase_alphabet = list(string.ascii_lowercase)




num1 = math.floor(random.random() * 26)
num1 = lowercase_alphabet[num1]

num2 = math.floor(random.random() * 26)
num2 = lowercase_alphabet[num2]

num3 = math.floor(random.random() * 26)
num3 = lowercase_alphabet[num3]

num4 = math.floor(random.random() * 26)
num4 = lowercase_alphabet[num4]

num5 = math.floor(random.random() * 26)
num5 = lowercase_alphabet[num5]

num6 = math.floor(random.random() * 26)
num6 = lowercase_alphabet[num6]

fullNumstart=num1+num2+num3
fullNumelast=num4+num5+num6

if (x == "encrypt"):
    text = input("Enter the text you wants to Encrypt: ")
    if(len(text)==2 ):
        encrypt =  text[::-1]
        print("Encrypted text is: ",encrypt)
    elif(len(text)>2):
        encrypt = fullNumstart+ text[1:len(text)] + text[0] + fullNumelast
        print("Encrypted text is: ",encrypt)
else:
    text = input("Enter the text you wants to Decrypt: ")
    if(len(text)==2):
        decrypt = text[::-1]
        print("Decrypted text is: ",decrypt)
    elif(len(text)>2):
        decrypt = text[len(text)-1:]+text[3:len(text)-1]
        print("Decrypted text is: ",decrypt)



      
