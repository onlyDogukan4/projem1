def repeater():
    my_str=""
    x=str(input("write sth here: "))
    t=len(x)
    for i in range(t):
        my_str=my_str+str(x[i]*2)
    return my_str
print(repeater())