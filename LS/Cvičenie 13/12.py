import tkinter

class Kocka:
  def __init__(self, x, y, hodnota):
    self.x = x
    self.y = y
    self.hodnota = hodnota

  def nakresli(self, canvas):
    canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill="red")

    canvas.create_text(self.x + 25, self.y + 25, text=str(self.hodnota), font=("Arial", 16))

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

kocka = Kocka(100, 100, 5)
kocka.nakresli(canvas)

canvas.mainloop()