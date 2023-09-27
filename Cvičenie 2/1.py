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


# 1
# int('123.456')
# int(123.456)
# float('123')
# float('123.456')
# int(float('123.456'))
# int('100') * 23
# int('100') + int('23')
# 100 * '23'

# 2
# k = 24
# k = 100 + k
# m = 5
# 1 + m = m # need to remove
# k = k + x
# m = input('zadaj text ')
# x = k + int(input('zadaj celé číslo '))
# print(x + ' hotovo')
# print(m + ' hotovo')


# # 3
# a = 1
# v = 0
# b = a + 1
# v = v + b
# b = b + a
# a = 4 * a + b * b
# v = v + a * b + 1
# # value of v is 42

# 4
# a = float(input('Zadaj dĺžku strany: '))
# obvod = 4 * a
# print('Obvod štvorca je', obvod)


# 5
# centy = int(input("Zadajte počet centov: "))
# eura = centy / 100
# print(f"{centy} centov = {eura} EUR")


# 6
# a = float(input("zadaj počet litrov: "))
# b = 1.5
# print(f"zaplatíš {a * b} €")

# 7
# a = int(input("Zadaj prvé číslo: "))
# b = int(input("Zadaj druhé číslo: "))
# print(f"priemer čísel {a} a {b} je {(a + b) / 2}")

# 8
# x = float(input("Zadajte x: "))
# vysledok = x ** 2 / 2 - 3 * x + 1
# print(f"Výsledok je {vysledok}")

# 9
# name = str(input("Napíš. ako sa voláš: "))
# print(f"Ahoj, {name}")

# 10
# import tkinter

# canvas = tkinter.Canvas(width=500, height=500)
# canvas.pack()
# a = int(input("Zadaj dĺžku strany: "))
# canvas.create_rectangle(0, 0, a, a)
# canvas.mainloop()

# 11
# import tkinter

# canvas = tkinter.Canvas(width=500, height=500)
# canvas.pack()
# a = int(input("Zadaj dĺžku strany: "))
# b = int(input("Zadaj dĺžku strany: "))
# canvas.create_rectangle(250 - a / 2, 250 - b / 2, 250 + a / 2, 250 + b / 2)
# canvas.mainloop()

# 12
import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()
a = str(input("Napíš. ako sa voláš: "))
canvas.create_text(250, 250, text=a)
canvas.mainloop()

# 13
# a = int(input("koľko zaplatíte za stravu za 1 týždeň: "))
# b = int(input("koľko zaplatíte za cestovné na 1 týždeň: "))
# c = int(input("koľko stojí ubytovanie na 1 mesiac: "))
# d = int(input("počet mesiacov, za ktoré chcete vypočítať náklady: "))
# print(f"náklady na štúdium počas {d} mesiacov sú {d * (a * 4 + b * 4 + c)}")





