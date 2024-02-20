import tkinter
import random

k = [[random.randint(0, 1) for _ in range(15)] for _ in range(10)]

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
                canvas.create_oval(x + 5, y + 5, x + 45, y + 45, fill="red", outline="")
                
    pocet()
    
def pocet():            
    poc = 1 
    for r in range(10):
        for s in range(15):
            if k[r][s] != 0:
                poc = 0  

    if poc == 1:
        canvas.create_rectangle(400, 250, fill="lightgrey", outline="")
        canvas.create_text(400, 250, text="Hurá!", font=('Helvetica', 32), fill='green')
    return poc

def reaction(r, s):
    count = 0
    for i in range(r-1, r+2):
        for j in range(s-1, s+2):
            if 0 <= i < 10 and 0 <= j < 15:
                count += k[i][j]

    if count > 3 and count <= 9:
        for i in range(r-1, r+2):
            for j in range(s-1, s+2):
                if 0 <= i < 10 and 0 <= j < 15:
                    k[i][j] = 0

def move_element(src_r, src_s, dest_r, dest_s):
    k[dest_r][dest_s] = k[src_r][src_s]
    k[src_r][src_s] = 0

def prvy_klik(r, s):
    global klik, r_start, s_start
    if k[r][s] == 1:
        klik = 1
        r_start, s_start = r, s
        canvas.create_rectangle(s * 50 + 2, r * 50 + 2, (s + 1) * 50 + 2, (r + 1) * 50 + 2, outline="blue", width=5 )

def druhy_klik(r, s):
    global klik
    if klik == 1:
        klik = 0
        if r_start == r or s_start == s or abs(r_start - r) == abs(s_start - s):
            reaction(r, s)
            move_element(r_start, s_start, r, s)
            kresli()

def press(event):
    global r_start, s_start
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
