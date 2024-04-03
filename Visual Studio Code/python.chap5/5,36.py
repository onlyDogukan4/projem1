live = 7
secretword = "metallica"
guesslist = []

while live > 0:
    t = 0
    x = str(input("Enter a letter: "))
    if x not in guesslist:
        guesslist.append(x)
    else:
        print("You already tried this letter.")

    for i in secretword:
        if i in guesslist:
            print(f"[ {i} ]", end=" ")
            t += 1
        else:
            print(f"[ - ]", end=" ")

    print()

    if x not in secretword:
        live -= 1
        print(f"You have {live} guesses left !!!")
        

    if t == len(secretword):
        print("You Won!")
        break

if live == 0:
    print("YOU LOST !!!")