import tkinter
import math

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def bodky():
    for i in range(7):
        x = 320 + 100 * math.cos(i * 2 * math.pi / 7)
        y = 240 + 100 * math.sin(i * 2 * math.pi / 7)
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')


bodky()

canvas.mainloop()
