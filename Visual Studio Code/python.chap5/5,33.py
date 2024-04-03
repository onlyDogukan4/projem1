def  getInt(min,max):
    while True:
        x=input("enter a number: ")
        try:
            x=int(x)  
            if min<x<max:
                print(f"{x} between 5 and 8")
                break
            else:    
                print(f"Your number must be between 5 and 8.")
        except:
            print("That is not a valid integer.")
print(getInt(5,8))