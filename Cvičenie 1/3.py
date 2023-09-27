# def logo():
#     print(
#         """

#   ▄▄▄█████▓ █    ██  ██▀███   ▄▄▄▄    ▒█████   ██▓███   ▄▄▄        ██████  ▄████▄   ▄▄▄       ██▓    
#   ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▓█████▄ ▒██▒  ██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██▒    
#   ▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒██▒ ▄██▒██░  ██▒▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▒██░    
#   ░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ▒██░█▀  ▒██   ██░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    
#     ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒░▓█  ▀█▓░ ████▓▒░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒░██████▒
#     ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▒▓███▀▒░ ▒░▒░▒░ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░
#       ░    ░░▒░ ░ ░   ░▒ ░ ▒░▒░▒   ░   ░ ▒ ▒░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░
#     ░       ░░░ ░ ░   ░░   ░  ░    ░ ░ ░ ░ ▒  ░░         ░   ▒   ░  ░  ░  ░          ░   ▒     ░ ░   
#               ░        ░      ░          ░ ░                 ░  ░      ░  ░ ░            ░  ░    ░  ░
#                                    ░                                      ░                          

                                                                          
#                                                                           """
#     )

# logo()
# a = str(input('Zadaj meno: '))
# print(f'Pozdravujem Ťa {a}')

# print('Obdĺžnik', 10 * 20 )
# print('Obdĺžnik so stranami 10 a 20 má obsah 10 * 20 =', 10 * 20 )
# print('Obdĺžnik so stranami 10 a 20 má obsah', 10*20, 'a jeho obvod je 2 * (10 + 20) =', 2 * (10 + 20))


# print(f'*' * 22)
# print(f'*' + ' ' * 20 + '*')
# print(f'*' + ' Uladzislau Novikau '+ '*')
# print(f'*' + ' ' * 20 + '*')
# print(f'*' * 22)

# print('(1 + 2) × (3 + 4) = ', (1 + 2) * (3 + 4))
# print('1 + 2')
# print('--- =', round((1+2)/(3+4), 2))
# print('3 + 4')


# print('súčet čísel 5 a 6 =', 5+6)
# print('súčet čísel od 1 po 10 =', sum(range(1, 11)))
# print('súčin zo súčtu a rozdielu čísel 3 a 4 = ', (3+4)*(3-4))


# print('Tento program pocita obsah kruhu')
# print('Kruh má polomer', 10)
# print('Obsah kruhu =', 3,14 * 10 * 10)

# import tkinter
# canvas = tkinter.Canvas(width=500, height=300)
# canvas.pack()
# canvas.create_rectangle(50, 50, 450, 250)
# canvas.mainloop()

# import tkinter
# canvas = tkinter.Canvas(width=500, height=300)
# canvas.pack()
# canvas.create_rectangle(200, 100, 300, 200, fill='black')
# canvas.mainloop()


# import tkinter
# canvas = tkinter.Canvas(width=850, height=300)
# canvas.pack()
# canvas.create_rectangle(375, 10, 425, 60, fill = "black") #head
# canvas.create_rectangle(350, 60, 450, 160, fill = "grey") #body
# canvas.create_rectangle(325, 60, 350, 160, fill = "black") #left hand
# canvas.create_rectangle(450, 60, 475, 160, fill = "black") #rigt hand
# canvas.create_rectangle(360, 160, 385, 260, fill = "grey") #left leg
# canvas.create_rectangle(415, 160, 440, 260, fill = "grey") #right leg
# canvas.mainloop()

# import tkinter
# canvas = tkinter.Canvas(width=500, height=300)
# canvas.pack()
# a = str(input('Zadaj meno: '))
# canvas.create_text(250, 150, fill = 'black', font = ('Arial', 20), text = f'Ahoj {a}! Ako sa máš?')
# canvas.mainloop()

# import tkinter
# canvas = tkinter.Canvas(width=500, height=300)
# canvas.pack()
# a = str(input('Zadaj meno: '))
# canvas.create_text(250, 150, fill = 'red', font = ('Times New Roman', 20), text = f'Ahoj {a}!')
# canvas.create_text(250, 200, fill = 'blue', font = ('Courier New', 20), text = f'Ako sa máš?')
# canvas.mainloop()


# import tkinter
# canvas = tkinter.Canvas(width=500, height=300)
# canvas.pack()
# canvas.create_text(50, 50, fill = 'green', font = ('Arial', 20), text = f'1')
# canvas.create_text(450, 50, fill = 'blue', font = ('Arial', 20), text = f'2')
# canvas.create_text(450, 250, fill = 'orange', font = ('Arial', 20), text = f'3')
# canvas.create_text(50, 250, fill = 'red', font = ('Arial', 20), text = f'4')
# canvas.mainloop()

# import tkinter as tk

# def create_text_with_shadow(canvas, x, y, text, font, text_color, shadow_color, shadow_offset):
#     canvas.create_text(x + shadow_offset, y + shadow_offset, text=text, font=font, fill=shadow_color)
#     canvas.create_text(x, y, text=text, font=font, fill=text_color)

# root = tk.Tk()
# root.title("Текст с тенью")

# canvas = tk.Canvas(root, width=400, height=200)
# canvas.pack()

# text = "Text s tieňom"
# font = ("Helvetica", 24)
# text_color = "black"
# shadow_color = "gray"
# shadow_offset = 4

# create_text_with_shadow(canvas, 100, 100, text, font, text_color, shadow_color, shadow_offset)

# root.mainloop()
