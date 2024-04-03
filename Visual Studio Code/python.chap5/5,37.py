from cs1graphics import *

def create_Stick(live, canvas=None):
    if canvas is None:
        canvas = Canvas(300, 400)
    
    canvas.clear()

    # Baş
    if live < 7:
        head = Circle(20)
        head.move(150, 50)
        canvas.add(head)

    # Gövde
    if live < 6:
        body = Square(40)
        body.move(150, 90)
        canvas.add(body)

    # Sağ Kol
    if live < 5:
        right_arm = Path(Point(170, 70), Point(180, 130))
        canvas.add(right_arm)

    # Sol Kol
    if live < 4:
        left_arm = Path(Point(130, 70), Point(120, 130))
        canvas.add(left_arm)

    # Sağ Bacak
    if live < 3:
        right_leg = Path(Point(150, 110), Point(170, 150))
        canvas.add(right_leg)

    # Sol Bacak
    if live < 2:
        left_leg = Path(Point(150, 110), Point(130, 150))
        canvas.add(left_leg)
    if live<1:
        head.moveTo(155,190)
        head.setFillColor("red")
    return canvas

def game():
    live = 7
    secretword = "metallica"
    guesslist = []
    canvas = create_Stick(live)

    while live > 0:
        t = 0
        x = str(input("Guess a letter: "))
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
        
        # Burada çizimi güncelliyoruz
        canvas = create_Stick(live, canvas)

        if t == len(secretword):
            print("You Won!")
            break

    if live == 0:
        print("YOU LOST !!!")

    canvas.wait()

game()
