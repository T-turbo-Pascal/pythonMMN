import tkinter

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()


def kruh(x, y, r, farba):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba)


def kvet(x, y, v, red_size):
    kruh(x, y - v, red_size, 'red')
    kruh(x, y + v, red_size, 'red')
    kruh(x - v, y, red_size, 'red')
    kruh(x + v, y, red_size, 'red')
    kruh(x, y, v, 'yellow')


kvet(100, 100, 40, 30) # left top
kvet(700, 100, 40, 30) # right top
kvet(100, 500, 40, 30) # left bottom
kvet(700, 500, 40, 30) # right bottom
kvet(400, 300, 40, 30) # center

canvas.mainloop()
