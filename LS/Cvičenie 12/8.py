def vytvor_presmycku(slovo):
    dlzka = len(slovo)
    polovica = dlzka // 2

    prva_cast = slovo[:polovica]
    druha_cast = slovo[polovica:]

    presmycka = druha_cast + prva_cast
    return presmycka

vstup = input("Zadaj slovo: ")

vysledok = vytvor_presmycku(vstup)

print(vysledok)
