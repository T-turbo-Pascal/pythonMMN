# 1
# sucet = 0
# for i in range(1, 1001):
#     sucet += 1/i
# print(sucet)


# 2
# n = int(input("faktoriál pre: "))
# faktorial = 1
# for i in range(1, n+1):
#     faktorial *= i
# print(f"{n}! = {faktorial}")

# 3
# for i in range(1, 101):
#     if i % 3 == 0 and i % 7 == 0:
#         print(i)

# 4
# n = int(input("prvé celé číslo: "))
# m = int(input("druhé celé číslo: "))
#
# podiel = 0
# zvysok = 0
#
# while n >= m:
#     n -= m
#     podiel += 1
#     zvysok = n
#
# print(f"podiel = {podiel} a zvyšok = {zvysok}")

# 5
# cislo = int(input("dvojciferné prirodzené číslo: "))
# sucet = 0
# while cislo > 0:
#     sucet += cislo % 10
#     cislo //= 10
# print(f"súčet cifier je {sucet}")

# 6
# for i in range(10, 100):
#     if (i % 10) + (i // 10) % 10 % 7 == 0:
#         print(i)

# 7
# pocet = int(input("počet zlomkov: "))
# sucet = 0
# for i in range(pocet):
#     citatel = int(input(f"{i+1}. zlomok: "))
#     menovatel = int(input(f"---\n"))
#     sucet += citatel / menovatel
# print(f"súčet = {sucet}")

# 8
#  НАДО СДЕЛАТЬ

# 9
# dlzka = 500
# sirka = 0
# vlak = 12
# while sirka + vlak <= dlzka:
#     sirka += vlak
#     vlak *= 2
#     print(f"vlak {vlak}")
#     print(f"sirka {sirka}")
#     print(f"dlzka {dlzka}")
#     print("-----")

# 10
# n = 0
# while n ** 3 <= 100:
#     n += 1
# print(n)

# 11
# a = int(input("dĺžka odstavnej koľaje: "))
# b = 12
# pocet = 0
# while a >= b:
#     a -= b
#     pocet += 1
# print(f"Na odstavnej koľaji sa zmestí {pocet} vlakov.")

# 14
# cislo = int(input("prirodzené číslo: "))
# sucet = 0
# while cislo > 0:
#     sucet += cislo % 10
#     cislo //= 10
# print(f"súčet cifier je {sucet}")

# 15
# c = 3 * 0.1
# print(0.25 + 0.25)
# print(2 * 0.1)
# print(format(c, '.1f'))
