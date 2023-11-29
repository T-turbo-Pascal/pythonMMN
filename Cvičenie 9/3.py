import tkinter

def nasobilka(pole):
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            pole[i][j] = (i + 1) * (j + 1)

def vypis(canvas, pole):
    canvas.delete("all")

    for i in range(len(pole)):
        for j in range(len(pole[i])):
            canvas.create_text(j * 40 + 20, i * 40 + 20, text=str(pole[i][j]))

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

nasobilka(a)

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

vypis(canvas, a)

canvas.mainloop()