#HANGMAN MODIFIED
import random
from cs1graphics import *
def draw_head(canvas):
    circle = Circle(50)
    circle.setBorderColor('black')
    canvas.add(circle)
    circle.moveTo(250, 100)

def hangman():
    canvas = Canvas(500,1250)
    difficulty = int(input("DIFFICULTY\nHow many letters should the word have?"))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word = "_"*difficulty
    word = list(word)
    answer = []

    for i in range(difficulty):
        answer += random.choice(alphabet)
    print(answer)
    counter = 0
    entered_letters = []
    while counter < 7 and word != answer:
        print(f"Entered letters: {entered_letters}")
        guess = input("Enter a letter:")
        while guess in entered_letters:
            guess = input(f"You've already entered {guess}. Please enter another latter:")
        entered_letters.append(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    word[i] = guess
            print(word)
        elif counter == 6:
            print("You are out of guesses. BOZGUN")
            break
        else:
            print(f"WRONG\nYou have {6-counter} guesses left.")
            counter += 1
        if word == answer:
            print("YOU WIN THE GAME")
            break
        if counter == 1:
            draw_head(canvas)

hangman()

