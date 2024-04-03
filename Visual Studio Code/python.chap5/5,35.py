def caller():
    my_str=""
    while True:
        number=input("enter a number: ")
        Index=input("enter a index: ")
        try:
            number=int(number)
            Index=int(Index)
            if number<0 or Index<0:
                print("number or Index mustn't be negative !!!")
            elif not 32>Index>2:
                print("index must be in interval 2,32")
            else:
                while number!=0:
                    remainder=number%Index
                    my_str = str(remainder) + my_str
                    number//=Index
                    return my_str
        except:
            print("invalid value !!!")
print(caller())
