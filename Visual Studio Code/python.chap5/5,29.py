def greater_index(data):
    value=int(input("enter a value: "))
    for i in data:
        if value<i:
            return(data.index(i))
        elif i>=data[-1]:
            return(len(data))
print(greater_index([1,5,8,9,13]))