import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

a = [20, 40, 60, 80, 100, 100, 80, 60, 40, 40, 60, 80, 100, 100, 120, 140, 160, 180, 200, 200]


def kresli():
    for i in range(len(a)):
        canvas.create_rectangle(i * 20, 500 - a[i], (i + 1) * 20, 500, fill="black")

def schody():
    for i in range(len(a)):
        a[i] = (i + 1) * 10
    kresli()

schody()

canvas.mainloop()