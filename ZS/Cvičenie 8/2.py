import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def kresli(event):
    canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="black")


canvas.bind("<B1-Motion>", kresli)

canvas.mainloop()
