import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def kresli(event):
    canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="black")
    kresli_cerveny_kruh(event.x, event.y)


def kresli_cerveny_kruh(x, y):
    canvas.create_oval(x + 97, y - 3, x + 103, y + 3, fill="red")


canvas.bind("<B1-Motion>", kresli)

canvas.mainloop()
