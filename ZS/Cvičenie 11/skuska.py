import tkinter
import random

# Initialize the matrix
k = [[random.randint(0, 1) for _ in range(15)] for _ in range(10)]



def kresli():
    canvas.delete("all")
    for r in range(10):
        y = (r * 50) + 2
        for s in range(15):
            x = (s * 50) + 2
            if k[r][s] == 0:
                canvas.create_rectangle(x, y, x + 50, y + 50, fill="", outline="lightgrey", width=3)
            if k[r][s] == 1:
                canvas.create_rectangle(x, y, x + 50, y + 50, fill="", outline="lightgrey", width=3)
                canvas.create_oval(x + 5, y + 5, x + 45, y + 45, fill="red", outline="")
    
    test(r, s)


def test(r, s):
    if all(k[r][i] == 1 for i in range(15)):
        for i in range(15):
            k[r][i] = 0

    if all(k[i][s] == 1 for i in range(10)):
        for i in range(10):
            k[i][s] = 0

    poc = 1
    for r in range(10):
        for s in range(15):
            if k[r][s] != 0:
                poc = 0
    if poc == 1:
        canvas.create_text(400, 250, text="Hurá!", font="Arial 50", fill="green")

def prvy(r, s):
    global klik
    if k[r][s] == 1:
        klik = 1
        canvas.create_oval(
            s * 50 + 2,
            r * 50 + 2,
            (s + 1) * 50 + 2,
            (r + 1) * 50 + 2,
            outline="blue",
            width=3,
        )


def druhy(r, s):
    global klik
    if klik == 1:
        if k[r][s] == 0:
            if r == r_start or s == s_start:
                k[r][s] = 1
                k[r_start][s_start] = 0
                klik = 0
                test(r, s)
                kresli()
        else:
            klik = 0
            kresli()



def press(event):
    global r_start, s_start
    r = event.y // 50
    s = event.x // 50
    if klik == 0:
        prvy(r, s)
        r_start, s_start = r, s
    elif klik == 1:
        druhy(r, s)


canvas = tkinter.Canvas(width=800, height=500)
canvas.pack()

klik = 0
r_start, s_start = 0, 0
kresli()
canvas.bind("<ButtonPress>", press)

canvas.mainloop()
