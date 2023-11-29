import tkinter

canvas = tkinter.Canvas(width=200, height=200)
canvas.pack()

k = [[0] * 10 for i in range(0, 10)]


def kresli():
    canvas.delete('all')
    for r in range(0, 10):
        y = r * 20
        for s in range(0, 10):
            x = s * 20
            if k[r][s] == 0:
                canvas.create_rectangle(x, y, x + 20, y + 20, fill='white', outline='silver')
            else:
                canvas.create_rectangle(x, y, x + 20, y + 20, fill='red', outline='silver')


def klik(event):
    if 0 <= event.x < 10 * 20 and 0 <= event.y < 10 * 20:
        s = event.x // 20
        r = event.y // 20

        for i in range(max(0, r - 1), min(10, r + 2)):
            for j in range(max(0, s - 1), min(10, s + 2)):
                k[i][j] = 1 - k[i][j]

        kresli()
        n = 0
        for r in range(0, 10):
            for s in range(0, 10):
                n = n + k[r][s]
        if n == 100:
            canvas.create_text(250, 150, fill='black', font=('Arial', 50), text='Gratulujem...')


canvas.bind('<ButtonPress>', klik)
kresli()

canvas.mainloop()
