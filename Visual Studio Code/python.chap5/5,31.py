def yes_or_no_Prompt():
    x=str(input("yes/no? :"))
    if x =="yes":
        return True
    if x =="no":
        return False
    else:
        print("Invalid answer try again yes/no? : ")
        yes_or_no_Prompt()
print(yes_or_no_Prompt())
