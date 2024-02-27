import tkinter as tk


class Bod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pohni(self):
        self.y += 25


bod_p = Bod(200, 50)
bod_d = Bod(300, 100)
print("Súradnice bodu 1 : ", bod_p.x, bod_p.y)
print("Súradnice bodu 2 : ", bod_d.x, bod_d.y)

bod_p.pohni()
bod_d.pohni()

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

canvas.create_line(bod_p.x, bod_p.y, bod_d.x, bod_d.y)
canvas.mainloop()
