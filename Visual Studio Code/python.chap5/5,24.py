def lenghtMin():
    my_str=str(input("enter a sentence here: "))
    listnum=[]
    liststr=[]
    for i in my_str.split(" "):
        liststr.append(i)
        leni=len(i)
        listnum.append(leni)
    a=min(listnum)
    b=listnum.index(a)
    return liststr[b]
print(lenghtMin())