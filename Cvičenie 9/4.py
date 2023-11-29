import tkinter

a = [[0, 2, 2, 2, 2, 2, 2, 0, 0, 0],
     [2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
     [0, 0, 2, 2, 2, 2, 2, 2, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
     [0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
     [0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]


def nasobilka(pole):
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            pole[i][j] = (i + 1) * (j + 1)



def vypis(canvas, pole):
    canvas.delete("all")

    for i in range(len(pole)):
        for j in range(len(pole[i])):
            canvas.create_text(j * 20 + 10, i * 20 + 10, text=str(pole[i][j]))


nasobilka(a)

canvas = tkinter.Canvas(width=200, height=200)
canvas.pack()

vypis(canvas, a)

canvas.mainloop()