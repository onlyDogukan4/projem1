def cheerland():
    sesli="a,e,f,h,I,l,m,n,o,r,s,x"
    my_str=str(input("enter a word: "))
    for i in my_str:
        if i in sesli:
            print(f"Gimme an {i.upper()}")
        else:
            print(f"Gimme a  {i.upper()}")
    return(f"What's spell?\n{my_str.upper()}")
print(cheerland())