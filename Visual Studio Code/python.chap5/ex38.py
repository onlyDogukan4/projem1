
from cs1graphics import *
def arrows(n):
    canvas = Canvas(400, 400)
    circle = Circle(20)
    circle.setFillColor('black')
    circle.moveTo(200, 200)
    canvas.add(circle)
    num_arrows = n

    for i in range(num_arrows):
        event = canvas.wait()
        if event.getDescription() == 'mouse click':
            end_point = event.getMouseLocation()
            draw_arrow(canvas, end_point)

def draw_arrow(canvas, end_point):
    start_point = Point(200, 200)
    arrow_path = Path(start_point, end_point)
    arrow_path.setArrows("last")
    arrow_path.setBorderColor('black')
    arrow_path.setBorderWidth(4)
    canvas.add(arrow_path)



arrows(5)
