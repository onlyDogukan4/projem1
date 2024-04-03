import turtle

def Lucifer():
    
    t = turtle.Turtle()
    t.speed(10)
    #kafa 

    t.width(1)
    t.circle(70,80)    
    t.right(90)
    t.circle(10,180)
    t.width(4)
    t.pencolor("green")
    t.right(90)
    t.circle(70,40)
    for i in range(13):
        t.right(90)
        t.forward(10)
        t.backward(10)
        t.right(-90)
        t.circle(70,9)    
    t.circle(70,40)
    t.width(1)
    t.pencolor("black")
    t.right(90)
    t.circle(10,180)
    t.right(90)
    t.circle(70,80)

    #gözler
    t.penup()
    t.goto(-20,70)
    t.pendown()
    t.fillcolor("black")
    t.width(10)
    t.circle(10)
    t.penup()
    t.goto(20,70)
    t.pendown()
    t.fillcolor("black")
    t.circle(10)
    #ağız

    t.penup()
    t.goto(-40,60)
    t.pendown()
    t.width(15)
    t.pencolor("red")
    t.right(60)
    t.circle(50,120)

    #gövde
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(150)
    t.width(1)
    t.pencolor("black")
    t.forward(10)
    t.forward(15)
    t.right(90)
    t.forward(70)
    t.left(100)
    t.forward(150)
    t.left(80)
    t.forward(100)
    t.left(80)
    t.forward(150)
    t.left(100)
    t.forward(70)
    t.right(90)
    t.forward(25)
    #kaşlar
    t.penup()
    t.goto(-5,100)
    t.pendown()
    t.width(4)
    t.left(40)
    t.circle(20,120)
    t.penup()
    t.goto(25,120)
    t.left(-160)
    t.pendown()
    t.circle(20,120)

    






    turtle.done()
Lucifer()


