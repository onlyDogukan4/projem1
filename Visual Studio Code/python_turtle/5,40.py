from cs1graphics import *

def draw_stick_figure():
    canvas = Canvas(300, 400)
    
    # Baş
    head = Circle(20)
    head.move(150, 50)
    canvas.add(head)
    
    # Gövde
    body = Square(40)
    body.move(150, 90)
    canvas.add(body)
    
    # Sağ Kol
    right_arm = Path(Point(170, 70), Point(180, 130))
    canvas.add(right_arm)
    
    # Sol Kol
    left_arm = Path(Point(130, 70), Point(120, 130))
    canvas.add(left_arm)
    
    # Sağ Bacak
    right_leg = Path(Point(150, 110), Point(170, 150))
    canvas.add(right_leg)
    
    # Sol Bacak
    left_leg = Path(Point(150, 110), Point(130, 150))
    canvas.add(left_leg)

    # Canvas'ı göster
    canvas.wait()

# Çöp Adam Çizme Fonksiyonunu Çağır
draw_stick_figure()
