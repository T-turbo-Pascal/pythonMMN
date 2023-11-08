import tkinter
import random

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def randomStairs():
    a = [random.randint(1, 200) for _ in range(20)]
    return a


def vyhlad(a):
    n = len(a)
    for i in range(1, n - 1):
        a[i] = (a[i - 1] + a[i] + a[i + 1]) / 3
    # prvý prvok
    a[0] = (a[0] + a[1]) / 2
    # posledný prvok
    a[n - 1] = (a[n - 2] + a[n - 1]) / 2
    return a


def drawStairs(a):
    for i in range(len(a)):
        canvas.create_rectangle(i * 20, 500 - a[i], (i + 1) * 20, 500, fill="black")


stairs = randomStairs()
smoothed_stairs = vyhlad(stairs)
drawStairs(smoothed_stairs)

canvas.mainloop()
