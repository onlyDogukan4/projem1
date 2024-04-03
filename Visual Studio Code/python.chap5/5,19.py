def öklid_alg(x,y):
    while x!=0:
        y,x=x,y%x
    return y
print(öklid_alg(36,27))
