def pocet_delitelov(cislo):
    pocet = 0
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            pocet += 1
    return pocet


def je_prvocislo(cislo):
    return pocet_delitelov(cislo) == 2


def pocet_prvocislenych_dvojic_v_rozsahu(od, do):
    pocet_dvojic = 0
    for i in range(od, do + 1):
        if je_prvocislo(i) and je_prvocislo(i + 2):
            pocet_dvojic += 1
    return pocet_dvojic


print(f'Pocet prvočíselných dvojčiat v rozsahu 1-100: {pocet_prvocislenych_dvojic_v_rozsahu(1, 100)}')

print(f'Pocet prvočíselných dvojčiat v rozsahu 1-1000: {pocet_prvocislenych_dvojic_v_rozsahu(1, 1000)}')

print(f'Pocet prvočíselných dvojčiat v rozsahu 1-10000: {pocet_prvocislenych_dvojic_v_rozsahu(1, 10000)}')
