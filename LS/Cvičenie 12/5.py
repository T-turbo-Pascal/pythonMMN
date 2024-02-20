sablona = 'Kde *, tam *, * raz jedno kráľovstvo.'
nahrada = 'bolo'
vysledok = ''

for znak in sablona:
    if znak == '*':
        vysledok += nahrada
    else:
        vysledok += znak

print(vysledok)
