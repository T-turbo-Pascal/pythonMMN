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


def vypis(canvas, pole):
    canvas.delete("all")

    for i in range(len(pole)):
        for j in range(len(pole[i])):
            canvas.create_text(j * 40 + 20, i * 40 + 20, text=str(pole[i][j]))


canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

vypis(canvas, a)

canvas.mainloop()
