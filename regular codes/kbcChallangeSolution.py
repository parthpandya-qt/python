question = [["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1],
            ["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1],
            ["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1],
            ["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1],
            ["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1],
            ["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1],
            ["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1],
            ["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1],
            ["what is the capital of India?","Delhi","Mumbai","Bhopal","Banglore",1]]

money = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000,500000000]

for i in range(0,len(question)):
    print(question[i][0])
    
    print("1.",question[i][1])
    print("2.",question[i][2])
    print("3.",question[i][3])
    print("4.",question[i][4])
    x = input("Enter the answer :")
    if(int(x)==question[i][5]):
        print("Correct answer")
        print("Money won :",money[i])
    else:
        if(int(x)!=question[0][5]):
            print("Wrong answer")
            print("Money won : 0")
            break
        else:   
            print("Wrong answer")
            print("Money won :",money[i-1])
            break
else:
    print("You won the game")   