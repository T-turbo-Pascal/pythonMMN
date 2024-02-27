import tkinter


class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y


bod = Bod(200, 50)
bod2 = Bod(300, 100)

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_line(bod.x, bod.y, bod2.x, bod2.y)

canvas.mainloop()
