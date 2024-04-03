import math
import turtle

def draw_arrow():
    turtle.left(90)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(10)
    turtle.right(90)

def draw_arrows(target_x, target_y):
    start_x = turtle.xcor()
    start_y = turtle.ycor()
    distance = math.sqrt((target_x - start_x) ** 2 + (target_y - start_y) ** 2)

    for _ in range(6):
        draw_arrow()
        turtle.up()
        turtle.goto(start_x, start_y)
        turtle.down()

        x_increment = (target_x - start_x) / distance
        y_increment = (target_y - start_y) / distance

        for _ in range(int(distance)):
            turtle.forward(1)
            turtle.xcor(turtle.xcor() + x_increment)
            turtle.ycor(turtle.ycor() + y_increment)

    draw_arrow()

def handle_click(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    draw_arrows(x, y)

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Shooting Arrows")
screen.bgcolor("white")
screen.tracer(0)

turtle.speed(0)
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()

turtle.onscreenclick(handle_click)

screen.mainloop()