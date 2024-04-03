def sum_of_squares():
    x=int(input("enter a positive integer: "))
    pointer=0
    for i in range(1,x+1):
        pointer+=i**2
    return pointer
print(sum_of_squares())
