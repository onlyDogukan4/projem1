from cs1graphics import *

def create_Stick(live):
    canvas=Canvas(300,400)
    # Baş
    if live<6:
        head = Circle(20)
        head.move(150, 50)
        canvas.add(head)
    
    # Gövde
    if live<5:
        body = Square(40)
        body.move(150, 90)
        canvas.add(body)
    
    # Sağ Kol
    if live<4:
        right_arm = Path(Point(170, 70), Point(180, 130))
        canvas.add(right_arm)
    
    # Sol Kol
    if live<3:
        left_arm = Path(Point(130, 70), Point(120, 130))
        canvas.add(left_arm)
        
    # Sağ Bacak
    if live<2:
        right_leg = Path(Point(150, 110), Point(170, 150))
        canvas.add(right_leg)
    
    # Sol Bacak
    if live<1:
        left_leg = Path(Point(150, 110), Point(130, 150))
        canvas.add(left_leg)
    canvas.wait()
  

def game():
    live=7
    secretword = "yarrak"
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
                print(f"[ {i} ]",end=" ")
                t += 1
            else:
                print(f"[ - ]",end=" ")
                
        print()  # Yeni satıra geç

        if x not in secretword:
            live -= 1
            print(f"you have {live} guesses left !!!")
            create_Stick(live)

        if t == len(secretword):
            print("You Won!")
            break
    if live == 0:
        print("YOU LOST !!!")

game()


