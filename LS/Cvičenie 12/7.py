import tkinter 
from random import randint

def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    
    color_code = "#{:02x}{:02x}{:02x}".format(red, green, blue)
    
    return color_code

def random_text(canvas, text, font_size):
    x = randint(50, 300)
    y = randint(50, 200)
    color = random_color()

    canvas.create_text(x, y, text=text, font=("Arial", font_size), fill=color)

def draw_advertisement(canvas, entry, font_size):
    canvas.delete("all")  
    advertisement_text = entry.get()

    for char in advertisement_text:
        random_text(canvas, char, font_size)


canvas = tkinter.Canvas(width=400, height=300)
canvas.pack()

entry_label = tkinter.Label(text="Zadajte reklamný text:")
entry_label.pack()

entry = tkinter.Entry()
entry.pack()

draw_button = tkinter.Button(text="Nakresliť reklamný nápis", command=lambda: draw_advertisement(canvas, entry, 14))
draw_button.pack()

canvas.mainloop()

