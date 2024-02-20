def pocet_delitelov(cislo):
    pocet = 0
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            pocet += 1
    return pocet


cislo = int(input("celé číslo: "))
if pocet_delitelov(cislo) == 2:
    print(cislo, "je prvočíslo")
else:
    print(cislo, "nie je prvočíslo")
