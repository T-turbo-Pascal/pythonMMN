def pocet_korenov(a, b, c):
    if a == 0:
        return None
    D = b ** 2 - 4 * a * c
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0


print(pocet_korenov(1, 0, 1))
