import tkinter 
from random import randint

def generate_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    
    color_code = "#{:02x}{:02x}{:02x}".format(red, green, blue)
    
    return color_code

def create_random_text(canvas, text, font_size):
    x = randint(50, 300)
    y = randint(50, 200)
    color = generate_random_color()

    canvas.create_text(x, y, text=text, font=("Arial", font_size), fill=color)


canvas = tkinter.Canvas(width=400, height=300)
canvas.pack()

advertisement_text = "Reklamný nápis"

for char in advertisement_text:
    create_random_text(canvas, char, 14)

canvas.mainloop()

