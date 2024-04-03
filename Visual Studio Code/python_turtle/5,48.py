import turtle

# Turtle nesnesi oluştur
pen = turtle.Turtle()

# Çizgi rengini değiştir
pen.pencolor("blue")

# Dolgu rengini değiştir
pen.fillcolor("yellow")

# Kare çizimi
pen.begin_fill()  # Dolguyu başlat
for _ in range(4):
    pen.forward(100)
    pen.right(90)
pen.end_fill()    # Dolguyu bitir

# Çizimi pencere üzerinde göster
turtle.mainloop()
