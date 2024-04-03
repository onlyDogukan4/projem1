def is_calculator(n):
    sum=0
    for i in range(n):
        if i%2==0:
            a=2*i+1
            sum+=4/a
        else:
            b=2*i+1
            sum+=-4/b
    return sum
print(is_calculator(1000000))