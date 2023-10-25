import tkinter

canvas = tkinter.Canvas(width=800, height=600)

canvas.pack()


def troj(x, y, dlzka):
    canvas.create_line(x, y, x + dlzka, y, x + dlzka / 2, y - dlzka * 0.866, x, y)


def stvor(x, y, dlzka):
    canvas.create_rectangle(x, y, x + dlzka, y + dlzka)


def dom(x, y, dlzka):
    stvor(x, y, dlzka)
    troj(x, y, dlzka)


dom(100, 100, 100)

canvas.mainloop()
