def scitaj(a, b):
    return a + b


def kviz():
    import random
    while True:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        vysledok = scitaj(a, b)
        odpoved = input(str(a) + " + " + str(b) + " = ")
        if odpoved == "":
            break
        if int(odpoved) == vysledok:
            print("áno, je to tak")
        else:
            print("nie, skús znovu")


kviz()
