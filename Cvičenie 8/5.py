import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()


def kresli(event):
    canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="black")
    kresli_cerveny_kruh(event.x, event.y)


def kresli_cerveny_kruh(x, y):
    stred_x = canvas.winfo_reqwidth() // 2

    symetricky_x = 2 * stred_x - x
    symetricky_y = y

    canvas.create_oval(symetricky_x - 3, symetricky_y - 3, symetricky_x + 3, symetricky_y + 3, fill="red")

    kresli_modry_kruh(x, y)
    kresli_modry_kruh(symetricky_x, symetricky_y)


def kresli_modry_kruh(x, y):
    stred_y = canvas.winfo_reqheight() // 2

    symetricky_x = x
    symetricky_y = 2 * stred_y - y

    canvas.create_oval(symetricky_x - 3, symetricky_y - 3, symetricky_x + 3, symetricky_y + 3, fill="blue")


def kresli_zeleny_kruh(x, y):
    stred_y = canvas.winfo_reqheight() // 2

    symetricky_x = x
    symetricky_y = 2 * stred_y - y

    canvas.create_oval(symetricky_x - 3, symetricky_y - 3, symetricky_x + 3, symetricky_y + 3, fill="green")


canvas.bind("<B1-Motion>", kresli)

canvas.mainloop()
