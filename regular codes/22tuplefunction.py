def average(*number):

    sum=0
    for i in number:
        sum=sum+i
        return sum/len(number)
    # print("Average is:",avg)

a=average(2,3,4,5,6,7,8,9,10)    
print(a)