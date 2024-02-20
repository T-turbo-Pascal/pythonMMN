import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

a = [1, 1]


def kresli():
    for i in range(len(a)):
        canvas.create_rectangle(i * 20, 500 - a[i] * 20, (i + 1) * 20, 500, fill="black")


def schody():
    for i in range(2, 20):
        a.append(a[i - 1] + a[i - 2])
    kresli()


schody()

canvas.mainloop()
