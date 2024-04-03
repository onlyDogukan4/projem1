def Decimal_Numbers():
    number=int(input("enter a number: "))
    Index=int(input("enter a index: "))
    my_str=""
    while number!=0:
        remainder=number%Index
        my_str = str(remainder) + my_str
        number//=Index
    return my_str
print(Decimal_Numbers())

        

