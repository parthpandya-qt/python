x = input("enter the number whose Table you wants to print  :")


try:
    print(f"table of {int(x)} is:")
    for i in range(1,11):
        print(f"{int(x)} x {i} = {int(x)*i}")
except:
    print("Please enter a valid number")


print("HELLO WORLD")            