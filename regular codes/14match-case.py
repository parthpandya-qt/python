x= int(input("enter the value greater than 0 :"))

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")        
    case _:
        print("no is greater than 4:")    