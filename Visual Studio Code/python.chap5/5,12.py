def GCD(x,y):
    iterations=-1
    while y!=0:
        x,y=y,x%y
        iterations+=1
    return(f"{iterations} times iterations")
print(GCD(18,48))