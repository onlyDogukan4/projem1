def toDecimal():
    string=str(input("enter a number: "))
    base=int(input("enter which based on index: "))
    digits ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = 0
    for digit in string:
        value = value * base + digits.index(digit)
    return value
print(toDecimal())