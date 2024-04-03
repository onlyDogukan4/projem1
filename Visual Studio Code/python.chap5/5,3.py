pointer=0
numbers=0
while 1:
    x=int(input("enter a number: "))
    if x !=0:
        pointer+=x
        numbers+=1
    else:
        print(pointer/numbers)
        break