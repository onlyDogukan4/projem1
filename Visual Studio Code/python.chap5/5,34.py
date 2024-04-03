def caller():
    while True:
        x=input("enter a word: ")
        number=input("enter a number: ")
        try:
            x=str(x)
            number=int(number)
            if number>=len(x):
                print("invalid number !!!")
            elif number<0:
                print("number must be positive !!!")
            else:
                for i in range(len(x)-number+1):
                    print(i*" "+x[i:i+number])
        except:                                                      
            print("invalid format !!!")
print(caller())