def fuc():

    try:
        num = int(input("Enter a integer  : "))
        a= [4,5,35,45,56,67,78,89]
        print(a[num])
        return 1
    except IndexError:
        print("Error: Index out of range")
        return 2
    finally:
        print("This block will always execute")    


print(fuc())
    

try:
    num = int(input("Enter a integer  : "))
    a= [4,5]
    print(a[num])
    
except IndexError:
    print("Error: Index out of range")
  
finally:
    print("This block will always execute")    