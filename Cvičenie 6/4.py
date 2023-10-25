# надо переделать
import tkinter

canvas = tkinter.Canvas(width=800, height=700)
canvas.pack()


def kruh(x, y, r, farba):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba)


kruh(200, 100, 50, 'aqua')
kruh(200, 250, 100, 'blue')
kruh(200, 480, 130, 'navy')

canvas.mainloop()
