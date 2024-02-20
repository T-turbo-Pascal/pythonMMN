import tkinter

canvas = tkinter.Canvas(width=500, height=100)
canvas.pack()

kamene = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def kresli():
    canvas.delete("all")
    for i in range(len(kamene)):
        if kamene[i] == 0:
            canvas.create_rectangle(i * 50, 0, (i + 1) * 50, 50, fill="grey")
        else:
            canvas.create_rectangle(i * 50, 0, (i + 1) * 50, 50, fill="red")


def otoc(index):
    if kamene[index] == 0:
        kamene[index] = 1
    else:
        kamene[index] = 0


def klik(event):
    index = event.x // 50
    otoc(index)
    kresli()
    if sum(kamene) == 10:
        print("Vyhral si!")


kresli()

canvas.bind("<Button-1>", klik)

canvas.mainloop()
