from random import *


def vymysli():
    global a, b
    a = randint(1, 10)
    b = randint(1, 10)
    print(f"{a} + {b} = ", end='')


def opytajsa():
    global vstup
    vstup = input()


vymysli()
opytajsa()
while vstup != '':
    if a + b == int(vstup):
        print('áno, je to tak')
        vymysli()
    else:
        print('nie, skús znovu')
    opytajsa()
