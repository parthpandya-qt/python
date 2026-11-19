try:
    num = int(input("Enter a integer  : "))
    a= [4,5]
    print(a[num])
except Exception as e:
    print("Error is : ", e)
except ValueError:
    print("Please enter a valid integer")
except IndexError:
    print("Please enter a valid index")    