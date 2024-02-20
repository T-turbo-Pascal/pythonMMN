import tkinter
import random

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def ramdomStairs():
    a = []
    for i in range(20):
        a.append(random.randint(1, 200))
    for i in range(len(a)):
        canvas.create_rectangle(i * 20, 500 - a[i], (i + 1) * 20, 500, fill="black")


ramdomStairs()

canvas.mainloop()
