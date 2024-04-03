def factorial():
    n=int(input("enter an positive integer: "))
    pointer=1
    while n>0:
        pointer*=n
        n=n-1
    return pointer
print(factorial())