def sliding():
    word=str(input("enter a word: "))
    num=int(input("enter how many numbers do you want: "))
    lenword=len(word)
    for i in range(lenword-num+1):
            print(i*" "+word[i:i+num])
print(sliding())
