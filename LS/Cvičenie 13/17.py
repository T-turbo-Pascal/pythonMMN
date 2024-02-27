import tkinter
import random

class Kocka:
    def __init__(self, x, y, hodnota):
        self.x = x
        self.y = y
        self.hodnota = hodnota

    def nakresli(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill="red")
        canvas.create_text(self.x + 25, self.y + 25, text=str(self.hodnota), font=("Arial", 16))

def kresli_vsetko(canvas, k1, k2, k3):
    canvas.delete("all")
    k1.nakresli(canvas)
    k2.nakresli(canvas)
    k3.nakresli(canvas)

def hod_kockami():
    k1.hodnota = random.randint(1, 6)
    k2.hodnota = random.randint(1, 6)
    k3.hodnota = random.randint(1, 6)

    if k1.hodnota == k2.hodnota and k2.hodnota == k3.hodnota:
        print("Hura!")
    else:
        print("Prehral si!")

    kresli_vsetko(canvas, k1, k2, k3)


canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

k1 = Kocka(100, 100, 6)
k2 = Kocka(160, 100, 6)
k3 = Kocka(220, 100, 6)

kresli_vsetko(canvas, k1, k2, k3)

# Pridanie tlačidla
hod_tlacitko = tkinter.Button(text="Hod Kockami", command=hod_kockami)
hod_tlacitko.pack()

canvas.mainloop()
