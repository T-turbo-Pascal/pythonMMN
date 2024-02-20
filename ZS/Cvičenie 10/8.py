# Dokončite predchádzajúci program tak, že zadefinujete funkciu f(x) = x2 / 300 - 100 a podprogramy krivka a graf. Podprogram krivka nakreslí krivku, ktorej priebeh zodpovedá funkcii f(x). Podprogram graf sa postará o nakreslenie celého grafu tým, že iba správne zavolá existujúce podprogramy.

# import tkinter
#
# canvas = tkinter.Canvas(width=640, height=480)
# canvas.pack()
#
# def osi():
#     canvas.create_line(20, 240, 620, 240)
#     canvas.create_line(320, 20, 320, 460)
#
# def znacky():
#     for i in range(0, 640, 10):
#         canvas.create_line(i, 235, i, 245)
#     for i in range(0, 480, 10):
#         canvas.create_line(315, i, 325, i)
#
# osi()
# znacky()
#
# canvas.mainloop()

import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def osi():
    canvas.create_line(20, 240, 620, 240)
    canvas.create_line(320, 20, 320, 460)


def znacky():
    for i in range(0, 640, 10):
        canvas.create_line(i, 235, i, 245)
    for i in range(0, 480, 10):
        canvas.create_line(315, i, 325, i)


def krivka():
    for x in range(-300, 301):
        y = x ** 2 / 300 - 100
        canvas.create_line(x + 320, -y + 240, x + 321, -y + 240)


def graf():
    osi()
    znacky()
    krivka()


graf()

canvas.mainloop()
