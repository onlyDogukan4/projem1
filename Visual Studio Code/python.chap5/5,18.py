def silly(x):
    print ('start silly')
    print (x)
    funny (2 *x)
    goofy (x-1)
    print ('end silly')
def funny(y):
    print ('start funny')
    print (y)
    goofy(y + 1)
    print ('end funny')
def goofy (z):
    print ('start goofy')
    print (z)
    print ('end goofy')
print(silly(5))
