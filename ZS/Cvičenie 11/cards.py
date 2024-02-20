import tkinter
import random

k = [[random.randint(0,1) for _ in range(15)] for _ in range(10)]


def kresli():
    canvas.delete('all')
    for r in range(10):
        y = (r*50)+2
        for s in range(15):
            x = (s*50)+2
            if k[r][s] == 0:
                canvas.create_rectangle(x, y, x + 50, y + 50, fill="", outline="lightgrey", width=3)
            if k[r][s] == 1:
                canvas.create_rectangle(x, y, x + 50, y + 50, fill="", outline="lightgrey", width=3)
                canvas.create_rectangle(x + 5, y + 5, x + 45, y + 45, fill="red", outline="")
    pocet()

def pocet():            
    poc = 1 
    for r in range(10):
        for s in range(15):
            if k[r][s] != 0:
                poc = 0  

    if poc == 1:
        canvas.create_text(400, 250, text="Hurá!", font=('Helvetica', 32), fill='green')
    return poc

def horz(r, od, kam):
    for s in range(od, kam + 1):
        k[r][s] = 1 - k[r][s]

def vert(s, of, kam):
    for r in range(of, kam + 1):
        k[r][s] = 1 - k[r][s]



def prvy_klik(r, s):
    global klik, r_start, s_start
    x = (s * 50) + 2
    y = (r * 50) + 2
    x1 = ((s + 1) * 50) + 2
    y1 = ((r + 1) * 50) + 2
    if k[r][s] == 1:
        klik = 1
        r_start, s_start = r, s
        canvas.create_rectangle(x,y,x1,y1,outline="grey",width=3)

def druhy_klik(r, s):
    global klik
    if klik == 1:
        klik = 0
        if r_start == r:
            horz(r, min(s_start, s), max(s_start, s))
        elif s_start == s:
            vert(s, min(r_start, r), max(r_start, r))
    kresli()
        
       

def press(event):
    r = event.y // 50
    s = event.x // 50
    if klik == 0:
        prvy_klik(r, s)
    elif klik == 1:
        druhy_klik(r, s)
                

canvas = tkinter.Canvas(width=800, height=500)
canvas.pack()

kresli()
klik = 0
r_start, s_start = 0, 0
canvas.bind("<ButtonPress>", press)

canvas.mainloop()
