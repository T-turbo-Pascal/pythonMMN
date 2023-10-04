def logo():
    print(
        """

  ▄▄▄█████▓ █    ██  ██▀███   ▄▄▄▄    ▒█████   ██▓███   ▄▄▄        ██████  ▄████▄   ▄▄▄       ██▓    
  ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▓█████▄ ▒██▒  ██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██▒    
  ▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒██▒ ▄██▒██░  ██▒▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▒██░    
  ░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ▒██░█▀  ▒██   ██░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    
    ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒░▓█  ▀█▓░ ████▓▒░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒░██████▒
    ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▒▓███▀▒░ ▒░▒░▒░ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░
      ░    ░░▒░ ░ ░   ░▒ ░ ▒░▒░▒   ░   ░ ▒ ▒░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░
    ░       ░░░ ░ ░   ░░   ░  ░    ░ ░ ░ ░ ▒  ░░         ░   ▒   ░  ░  ░  ░          ░   ▒     ░ ░   
              ░        ░      ░          ░ ░                 ░  ░      ░  ░ ░            ░  ░    ░  ░
                                   ░                                      ░                          


                                                                          """
    )


#  1

# for i in range(7):
#     print("*" * 20)

# ================================================================================================================

#   2

# for x in range(10):
#     x = (x + 10) / (10 - x)
#     x = float('{:.3f}'.format(x))
#     print(x)

# ================================================================================================================

#    3

# for x in range(10):
#     numerator = x + 10
#     denominator = 10 - x
#     result = float(numerator) / denominator
#     result = round(result, 1)
#
#     print(f"{numerator} + {denominator}\n------ = {result}\n{denominator} - {numerator}\n")

# ================================================================================================================

#    4

# n = int(input("Zadaj číslo: "))
# for i in range(1, 11):
#     print(f"{i} * {n} = {n * i}")

# ================================================================================================================

#    5

# import tkinter
#
# canvas = tkinter.Canvas(width=650, height=150)
#
# for i in range(10):
#     canvas.create_oval(10 + i * 60, 10, 70 + i * 60, 70, fill="black")
#
# canvas.pack()
# canvas.mainloop()


# ================================================================================================================

#    6

# import tkinter
# import random
#
# canvas = tkinter.Canvas(width=800, height=600)
#
# for i in range(10):
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#
#     fill_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)
#
#     x1 = i * 60
#     x2 = 60 + i * 60
#     canvas.create_oval(x1, 10, x2, 70, fill=fill_color)
#
# canvas.pack()
# canvas.mainloop()


# ================================================================================================================

#   7

# import tkinter
# import random
#
# canvas = tkinter.Canvas(width=800, height=600)
#
# for i in range(100):
#     canvas.create_text(random.randint(0, 800), random.randint(0, 600), text="*", fill='black', font=('Arial', 20))
#
# canvas.pack()
# canvas.mainloop()

# ================================================================================================================

#   8

# import tkinter
# import random
#
# canvas = tkinter.Canvas(width=800, height=600)
#
# canvas.create_rectangle(0, 0, 800, 600, fill='blue')
#
# for i in range(100):
#     canvas.create_text(random.randint(0, 800), random.randint(0, 600), text="*", fill='white',
#                        font=('Arial', random.randint(10, 50)))
#
# canvas.pack()
# canvas.mainloop()

# ================================================================================================================

#   9

# from random import *
# from tkinter import *
#
# canvas = Canvas(width=500, height=300, highlightthickness=0)
# canvas.pack()
#
# for i in range(0, 1000):
#     x = randrange(0, 51) * 10
#     y = randrange(0, 31) * 10
#
#     canvas.create_rectangle(x, y, x + 10, y + 10, fill='#%06x' % randrange(0, 0x01000000))
#
# mainloop()

# ================================================================================================================

#   10

# import tkinter
#
# canvas = tkinter.Canvas(width=700, height=150)
#
# for i in range(1, 11):
#     canvas.create_text(i * 60, 60, text=i, fill='black', font=('Arial', 20))
#
# canvas.pack()
# canvas.mainloop()

# ================================================================================================================

#   11

# import tkinter
#
# canvas = tkinter.Canvas(width=900, height=150)
#
# n = int(input("Zadaj číslo: "))
# for i in range(1, 11):
#     canvas.create_text(i * 80, 60, text=f"{i} * {n}", fill='black', font=('Arial', 20))
#
# for i in range(1, 11):
#     canvas.create_text(i * 80, 120, text=f"{n * i}", fill='black', font=('Arial', 20))
#
# canvas.pack()
# canvas.mainloop()

#  ================================================================================================================

#  12

# nothing output
# from tkinter import *
# canvas = Canvas(width = 500, height = 300, highlightthickness = 0)
# canvas.pack()
# for i in range(1, 101):
#     canvas.create_line(100 + i, 100, 100 + i, 100 + i, fill = 'black')

# ================================================================================================================


#  13

# import tkinter
#
# canvas = tkinter.Canvas(width=400, height=200)
# canvas.pack()
#
# stripe_height = canvas.winfo_reqheight() / 13
# stripe_color = 'red'
#
# for i in range(13):
#     y1 = i * stripe_height
#     y2 = (i + 1) * stripe_height
#     canvas.create_rectangle(0, y1, canvas.winfo_reqwidth(), y2, fill=stripe_color, outline=stripe_color)
#     if stripe_color == 'red':
#         stripe_color = 'white'
#     else:
#         stripe_color = 'red'
#
# blue_width = canvas.winfo_reqwidth() * 2 / 5
# blue_height = stripe_height * 7
# canvas.create_rectangle(0, 0, blue_width, blue_height, fill='blue', outline='blue')
#
# star_size = blue_height / 10
# for row in range(9):
#     for col in range(11):
#         if (row + col) % 2 == 0:
#             x = col * (blue_width / 11) + 7
#             y = row * (blue_height / 9) + 3
#             canvas.create_text(x, y, text='*', font=("Arial", 20), fill='white')
#
# canvas.mainloop()
