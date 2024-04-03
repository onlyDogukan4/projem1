from cs1graphics import *

def arrow(n):
    canvas=Canvas(400,400)

    circle=Circle(20)
    circle.move(200,200)
    circle.setFillColor("black")
    canvas.add(circle)

    num_arrows=n

    for i in range(num_arrows):
        event=canvas.wait()
        if event.getDescription()=="mouse click":
            endpoint=event.getMouseLocation()
            drawarrow(canvas,endpoint)
def drawarrow(canvas,endpoint):
