from cs1graphics import *

def arrows():
    canvas=Canvas(1000,1000)

    #kafa
    circle=Circle(70)
    circle.setFillColor("black")
    circle.setBorderColor("black")
    circle.moveTo(500,200)
    canvas.add(circle)

    #gövde
    body=Path(Point(500,270),Point(500,550))
    body.setBorderWidth(4)
    canvas.add(body)

    #sol bacak
    leftleg=Path(Point(500,550),Point(420,700))
    leftleg.setBorderWidth(4)
    canvas.add(leftleg)

    #sağ bacak

    leftleg=Path(Point(500,550),Point(580,700))
    leftleg.setBorderWidth(4)
    canvas.add(leftleg)

    #sol kol
    leftarm=Path(Point(500,330),Point(430,400))
    leftarm.setBorderWidth(4)
    canvas.add(leftarm)

    #sağ kol
    rightarm=Path(Point(500,330),Point(570,400))
    rightarm.setBorderWidth(4)
    canvas.add(rightarm)
    
arrows()
