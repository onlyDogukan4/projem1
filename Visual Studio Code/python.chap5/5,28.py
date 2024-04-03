def function():  
    list2=[]
    list=[5,3,8,2,9,1]
    Value=int(input("enter a value: "))
    pointer=0
    for i in list:
        if pointer<Value:
            pointer+=i
            list2.append(list.index(i))
    return(len(list2))
print(function())