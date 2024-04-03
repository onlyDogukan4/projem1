list=[]
pointer=0
while 1:
    x=str(input("enter a word: "))
    if x not in list:
        list.append(x)
        pointer+=1
        print(f"{list[-1]} added and you have {pointer} index in your list")
    else:
        print("already exist in your list")