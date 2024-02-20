import tkinter
import random

k = [[random.randint(0, 1) for _ in range(15)] for _ in range(10)]

def kresli():
    canvas.delete("all")
    for r in range(10):
        y = (r*50)+2
        for s in range(15):
            x = (s*50)+2
            if k[r][s] == 1:
                canvas.create_rectangle(x,y,x+50,y+50,outline="grey")
                canvas.create_oval(x+5,y+5,x+45,y+45,fill="red")
            else:
                canvas.create_rectangle(x,y,x+50,y+50,outline="grey")

    pocet()

def pocet():
    poc = 1
    for r in range(10):
        for s in range(15):
            if k[r][s] != 0:
                poc = 0
    if poc == 1:
        canvas.create_text(400,250,text="Hura!",font=("Arial",32),fill="green")
    return poc

def reakcia(r, s):
    count = 0
    for i in range(max(0, r-1), min(10, r+2)):
        for j in range(max(0, s-1), min(15, s+2)):
            count += k[i][j]
    if 3 <= count <= 9:
        for i in range(max(0, r-1), min(10, r+2)):
            for j in range(max(0, s-1), min(15, s+2)):
                k[i][j] = 0

def prvy(r,s):
    global klik, r_st, s_st
    if k[r][s] == 1:
        klik = 1
        r_st, s_st = r, s
        canvas.create_rectangle(
            (s*50)+2,
            (r*50)+2,
            ((s+1)*50)+2,
            ((r+1)*50)+2,
            outline="blue",
            width=3
            )

def druhy(r,s):
    global klik, r_st, s_st
    if klik == 1:
        klik = 0
        reakcia(r,s)
        k[r][s] = k[r_st][s_st]
        k[r_st][s_st] = 0
        kresli()

def press(event):
    global klik
    r = event.y // 50
    s = event.x // 50
    if klik == 0:
        prvy(r,s)
    elif klik == 1:
        druhy(r,s)
        
    

canvas = tkinter.Canvas(width = 800, height = 800, highlightthickness = 0)
canvas.pack()

kresli()
klik = 0
r_st, s_st = 0, 0
canvas.bind('<ButtonPress>', press)

canvas.mainloop()
