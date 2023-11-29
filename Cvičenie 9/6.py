import tkinter

obr = [
    [0, 2, 2, 2, 2, 2, 2, 0, 0, 0],
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
            if pole[i][j] == 1:
                canvas.create_rectangle(j * 40, i * 40, j * 40 + 40, i * 40 + 40, fill="green")
            elif pole[i][j] == 2:
                canvas.create_rectangle(j * 40, i * 40, j * 40 + 40, i * 40 + 40, fill="red")

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

vypis(canvas, obr)

canvas.mainloop()

