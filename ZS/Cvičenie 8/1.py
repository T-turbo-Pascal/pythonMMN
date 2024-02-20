import tkinter

canvas = tkinter.Canvas(width=500, height=100)
canvas.pack()


def sucet():
    a = int(entry1.get())
    b = int(entry2.get())
    canvas.create_text(250, 50, text=f"{a} + {b} = {a + b}", font="Arial 20")


label1 = tkinter.Label(text="Prvé číslo:")
label1.pack(side=tkinter.LEFT)
entry1 = tkinter.Entry(takefocus=True)
entry1.pack(side=tkinter.LEFT)

label2 = tkinter.Label(text="Druhé číslo:")
label2.pack(side=tkinter.LEFT)
entry2 = tkinter.Entry(takefocus=True)
entry2.pack(side=tkinter.LEFT)

button = tkinter.Button(text="Súčet", command=sucet)
button.pack(side=tkinter.LEFT)

canvas.mainloop()
