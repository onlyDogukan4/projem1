def PairSum(): 
    list=[5, 12, 3, 8, 1, 11, 7, 6, 17, 11]
    goal=int(input("enter a number: "))
    list=set(list)
    for i in list:
        if goal-i in set(list):
            return(f"({i},{goal-i})")
print(PairSum())