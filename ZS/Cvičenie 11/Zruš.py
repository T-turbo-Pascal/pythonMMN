import tkinter

kamene = [
    ["C", "C", " ", " ", " ", " ", " ", " ", "C", "C"],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "B", "B", " ", " ", " ", " ", " ", " "],
    [" ", " ", "B", "B", "A", "A", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "A", "A", "B", "B", " "],
    [" ", " ", " ", " ", " ", " ", " ", "B", "B", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["C", "C", " ", " ", " ", " ", " ", " ", "C", "C"],
]


def kresli():
    for i in range(10):
        for j in range(10):
            color = "white" if kamene[i][j] == " " else "yellow"
            canvas.create_rectangle(
                j * 40, i * 40, (j + 1) * 40, (i + 1) * 40, fill=color, outline="gray"
            )
            if kamene[i][j] != " ":
                canvas.create_text(
                    (j + 0.5) * 40,
                    (i + 0.5) * 40,
                    text=kamene[i][j],
                    font=("Helvetica", 16),
                )


def pocet_kamenov():
    count = sum(row.count(" ") for row in kamene)
    print(count)
    return 100 - count


def pocet_susedov(r, s):
    symbol = kamene[r][s]
    count = 0

    if r > 0 and kamene[r - 1][s] == symbol:
        count += 1
    if r < 9 and kamene[r + 1][s] == symbol:
        count += 1
    if s > 0 and kamene[r][s - 1] == symbol:
        count += 1
    if s < 9 and kamene[r][s + 1] == symbol:
        count += 1

    return count


def prvy_klik(r, s):
    global prvy
    prvy = (r, s)
    canvas.create_rectangle(
        s * 40, r * 40, (s + 1) * 40, (r + 1) * 40, outline="blue", width=2
    )


def druhy_klik(r, s):
    global druhy, klik, prvy

    druhy = (r, s)

    if (
        prvy is not None
        and prvy != druhy
        and kamene[prvy[0]][prvy[1]] == kamene[druhy[0]][druhy[1]]
        and pocet_susedov(prvy[0], prvy[1]) > 0
        and abs(prvy[0] - druhy[0]) + abs(prvy[1] - druhy[1]) == 1
    ):
        kamene[prvy[0]][prvy[1]] = " "
        kamene[druhy[0]][druhy[1]] = " "
    else:
        klik = 0

    prvy = None
    druhy = None
    kresli()


    if pocet_kamenov() == 0:
        canvas.create_text(200, 200, text="Hurá!", font=("Helvetica", 24), fill="green")
    elif all(
        kamene[i][j] == " " or pocet_susedov(i, j) == 0
        for i in range(10)
        for j in range(10)
    ):
        canvas.create_text(200, 200, text="Smola...", font=("Helvetica", 24), fill="red")


def press(event):
    global klik, prvy
    r = event.y // 40
    s = event.x // 40

    if klik == 0 and kamene[r][s] != " " and pocet_susedov(r, s) > 0:
        prvy_klik(r, s)
        klik = 1
    elif klik == 1:
        druhy_klik(r, s)
        klik = 0


canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

kresli()
klik = 0

canvas.bind("<Button-1>", press)

canvas.mainloop()
