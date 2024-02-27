import tkinter as tk


class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pohni(self):
        self.y += 25


bod1 = Bod(200, 50)
bod2 = Bod(300, 100)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()
canvas.create_line(bod1.x, bod1.y, bod2.x, bod2.y)

bod1.pohni()
bod2.pohni()
canvas.create_line(bod1.x, bod1.y, bod2.x, bod2.y, fill="black")

for i in range(3):
    bod1.pohni()
bod2.pohni()
canvas.create_line(bod1.x, bod1.y, bod2.x, bod2.y, fill="black")

canvas.mainloop()
