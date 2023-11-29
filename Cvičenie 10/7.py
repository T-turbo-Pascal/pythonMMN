import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def osi():
    canvas.create_line(20, 240, 620, 240)
    canvas.create_line(320, 20, 320, 460)


def znacky():
    for i in range(0, 640, 10):
        canvas.create_line(i, 235, i, 245)
    for i in range(0, 480, 10):
        canvas.create_line(315, i, 325, i)


osi()
znacky()

canvas.mainloop()
