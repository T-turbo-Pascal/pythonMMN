import tkinter

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()


def vypis(x, y, cislo):
    canvas.create_text(x, y, text=cislo)


for i in range(1, 11):
    vypis(100, 100 + 20 * i, i)
    vypis(120, 100 + 20 * i, i * i)

canvas.mainloop()
