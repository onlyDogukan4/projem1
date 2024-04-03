def base_of_numbers(number,base):
    t=number
    if number<0:
        return("does not support negative numbers")
    if number==0:
        return 0
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mystr="" 
    while number>0:
        a=number%base
        mystr= digits[a] + mystr
        number//=base
    return (f"The number {t} represented in base {base} seems like this {mystr}")
print(base_of_numbers(64180,16))