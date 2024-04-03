import turtle

# Turtle nesnesi oluştur
pen = turtle.Turtle()

# Yüz çizimi fonksiyonu
def draw_face():
    # Baş çizimi
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.circle(100)

    # Göz çizimi
    pen.penup()
    pen.goto(-40, 20)
    pen.pendown()
    pen.circle(10)
    
    pen.penup()
    pen.goto(40, 20)
    pen.pendown()
    pen.circle(10)

    # Ağız çizimi
    pen.penup()
    pen.goto(-40, -30)
    pen.pendown()
    pen.right(90)
    pen.circle(40, 180)

# Ana program
if __name__ == "__main__":
    turtle.speed(1)  # Çizim hızı ayarı
    draw_face()

    # Çizimi pencere üzerinde göster
    turtle.mainloop()
