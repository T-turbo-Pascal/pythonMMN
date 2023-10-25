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

# 1 
# a = int(input("Zadaj celé číslo: "))
# if a > 0:
#     print(f"{a} je kladné číslo")
# else:
#     print(f"{a} nie je kladné číslo")

# 2
# a = int(input("Zadaj celé číslo: "))
# if a > 0:
#     print(f"{a} je kladné číslo")
# elif a == 0:
#     print(f"{a} je nula")
# else:
#     print(f"{a} je záporné číslo")

# 3
# a = int(input("Zadaj prvé celé číslo: "))
# b = int(input("Zadaj druhé celé číslo: "))
# if a < b:
#     print(f"{a} < {b}")
# elif a == b:
#     print(f"{a} = {b}")
# else:
#     print(f"{a} > {b}")

# 4
# import random
#
# if random.randint(0, 1) == 0:
#     print("Tvoj počítač má zlú náladu.")
# else:
#     print("Tvoj počítač má radosť.")

# 5
# import tkinter
#
# canvas = tkinter.Canvas(width=800, height=400)
#
# a = int(input("Zadaj dĺžku prvej strany: "))
# b = int(input("Zadaj dĺžku druhej strany: "))
# if a >= b:
#     canvas.create_rectangle(10, 10, a, b, fill="black")
# else:
#     canvas.create_rectangle(10, 10, b, a, fill="black")
#
# canvas.pack()
# canvas.mainloop()

# 6
# import tkinter
# import random
#
# canvas = tkinter.Canvas(width=800, height=400)
#
# if random.randint(0, 1) == 0:
#     canvas.create_text(400, 200, text="Programovanie", fill="blue")
# else:
#     canvas.create_text(400, 200, text="Python", fill="red")
#
# canvas.pack()
# canvas.mainloop()

# 7
# import tkinter
# import random
#
# canvas = tkinter.Canvas(width=800, height=400)
#
# for i in range(100):
#     if random.randint(0, 1) == 0:
#         canvas.create_text(random.randint(0, 800), random.randint(0, 400), text="Programovanie", fill="blue")
#     else:
#         canvas.create_text(random.randint(0, 800), random.randint(0, 400), text="Python", fill="red")
#
# canvas.pack()
# canvas.mainloop()

# 8
# import tkinter
#
# canvas = tkinter.Canvas(width=300, height=400)
#
# a = int(input("Zadaj číslo od 1 do 6: "))
# bg = canvas.create_rectangle(20, 20, 160, 150, fill="white")
# if a == 1:
#     bg
#     canvas.create_oval(80, 80, 100, 100, fill="red")
# elif a == 2:
#     bg
#     canvas.create_oval(40, 40, 60, 60, fill="red")
#     canvas.create_oval(120, 120, 140, 140, fill="red")
# elif a == 3:
#     bg
#     canvas.create_oval(40, 40, 60, 60, fill="red")
#     canvas.create_oval(80, 80, 100, 100, fill="red")
#     canvas.create_oval(120, 120, 140, 140, fill="red")
# elif a == 4:
#     bg
#     canvas.create_oval(40, 40, 60, 60, fill="red")
#     canvas.create_oval(120, 40, 140, 60, fill="red")
#     canvas.create_oval(40, 120, 60, 140, fill="red")
#     canvas.create_oval(120, 120, 140, 140, fill="red")
# elif a == 5:
#     bg
#     canvas.create_oval(40, 40, 60, 60, fill="red")
#     canvas.create_oval(120, 40, 140, 60, fill="red")
#     canvas.create_oval(40, 120, 60, 140, fill="red")
#     canvas.create_oval(120, 120, 140, 140, fill="red")
#     canvas.create_oval(80, 80, 100, 100, fill="red")
# elif a == 6:
#     bg
#     canvas.create_oval(40, 40, 60, 60, fill="red")
#     canvas.create_oval(120, 40, 140, 60, fill="red")
#     canvas.create_oval(40, 120, 60, 140, fill="red")
#     canvas.create_oval(120, 120, 140, 140, fill="red")
#     canvas.create_oval(40, 80, 60, 100, fill="red")
#     canvas.create_oval(120, 80, 140, 100, fill="red")
# else:
#     print("Zadal si zlé číslo")
# canvas.pack()
# canvas.mainloop()


# 9
# import random
#
# user_input = input("Zadaj k, p alebo n: ")
# computer_input = random.choice(["k", "p", "n"])
#
# print(f"Počítač zvolil {computer_input}")
#
# if user_input == computer_input:
#     print("Remiza")
# elif user_input == "k" and computer_input == "p":
#     print("Vyhral som")
# elif user_input == "k" and computer_input == "n":
#     print("Vyhral si")
# elif user_input == "p" and computer_input == "k":
#     print("Vyhral si")
# elif user_input == "p" and computer_input == "n":
#     print("Vyhral som")
# elif user_input == "n" and computer_input == "k":
#     print("Vyhral som")
# elif user_input == "n" and computer_input == "p":
#     print("Vyhral si")
# else:
#     print("Zadal si zlé písmenko")

# 10
# Bez použitia počítača zistite, čo program vypíše: 52

