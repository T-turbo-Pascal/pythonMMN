import tkinter


class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pohni(self):
        self.y += 25

    def kresli(self):
        canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill="black")


def zmen():
    bod2.pohni()
    canvas.create_line(bod1.x, bod1.y, bod2.x, bod2.y, fill="black")
    bod2.kresli()


bod1 = Bod(200, 50)
bod2 = Bod(300, 100)

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()
canvas.create_line(bod1.x, bod1.y, bod2.x, bod2.y)

bod1.pohni()
bod2.pohni()
canvas.create_line(bod1.x, bod1.y, bod2.x, bod2.y, fill="black")

for i in range(3):
    bod1.pohni()
bod2.pohni()
canvas.create_line(bod1.x, bod1.y, bod2.x, bod2.y, fill="black")

bod1.kresli()
bod2.kresli()

button = tkinter.Button(text="Zmen", command=zmen)
button.pack()

canvas.mainloop()
