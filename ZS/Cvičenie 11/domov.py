import tkinter

k = [[2, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 2, 2, 1, 0, 0],
    [0, 0, 1, 2, 2, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 2]]

def kresli():
    canvas.delete("all")
    for r in range(8):
        y=(r*50)+2
        for s in range(8):
            x=(s*50)+2
            if k[r][s] == 0:
                canvas.create_rectangle(x,y,x+50,y+50,fill="",outline="lightgrey",width=3)
            if k[r][s] == 1:
                canvas.create_rectangle(x,y,x+50,y+50,fill="",outline="lightgrey",width=3)
                canvas.create_oval(x+5,y+5,x+45,y+45,fill="red",outline="")
            if k[r][s] == 2:
                canvas.create_rectangle(x,y,x+50,y+50,fill="yellow",outline="lightgrey",width=3)
            if k[r][s] == 3:
                canvas.create_rectangle(x,y,x+50,y+50,fill="yellow",outline="lightgrey",width=3)
                canvas.create_oval(x+5,y+5,x+45,y+45,fill="red",outline="")
    pocet_mimo()

def pocet_mimo():
    poc = 0
    fin = 0
    for r in range(8):
        for s in range(8):
            if k[r][s] == 1:
                poc = poc + 1
            if k[r][s] == 3:
                fin = fin + 1
    if fin == 8:
        canvas.create_text(200, 200, text="Hurá!", font=('Helvetica', 24), fill='green')
    return poc
    
def press(event):
    global klik
    r=event.y//50
    s=event.x//50
    if klik == 0:
        prvy(r,s)
    if klik == 1:
        druhy(r,s)

def prvy(r,s):
    global klik, r1, s1
    if k[r][s] == 1 or  k[r][s] == 3:
        r1 = r
        s1 = s
        klik = 1
    
def druhy(r,s):
    global klik, r1, s1
    if k[r][s] == 0 or k[r][s] == 2:
        klik = 0
    if k[r][s] == 1 or k[r][s] == 3:
        klik = 0
        prvy(r,s)
    
    r2 = r
    s2 = s
    if s1 == s2:
        ver(s1,r1,r2)
    if r1 == r2:
        hor(r1,s1,s2)

def ver(s,od,kam):
    n = (abs(kam-od))-1
    a = 0
    if od > kam:
        r = kam + 1
    else:
        r = od + 1
    for i in range (n):
        if k[r][s] == 0 or k[r][s] == 2:
            r = r+1
            a = a+1
        if k[r][s] == 1 or k[r][s] == 3:
            break
    if a == n:
        k[od][s] = k[od][s] - 1
        k[kam][s] = k[kam][s] + 1
        kresli()

def hor(r,od,kam):
    n = (abs(kam-od))-1
    a = 0
    if od > kam:
        s = kam + 1
    else:
        s = od + 1
    for i in range (n):
        if k[r][s] == 0 or k[r][s] == 2:
            s = s+1
            a = a+1
        if k[r][s] == 1 or k[r][s] == 3:
            break
    if a == n:
        k[r][od] = k[r][od] - 1
        k[r][kam] = k[r][kam] + 1
        kresli()
    
canvas=tkinter.Canvas(width=400,height=400,bg="white")
canvas.pack()

klik = 0
kresli()
canvas.bind('<ButtonPress>', press)

canvas.mainloop()

