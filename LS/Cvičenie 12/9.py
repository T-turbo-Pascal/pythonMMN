text = 'aaa'
n = 1
m = 1
for i in range(1, len(text)):
    if text[i - 1] != text[i]:
        n = 1
    else:
        n = n + 1
        if m < n:
            m = n
print(m)

# Prvý prípad (text = 'ababbc'):
# - Program vypíše 2.

# Druhý prípad (text = 'abaacccccbcbbacccabcb'):
# - Program vypíše 5.

# Všeobecná charakteristika programu:
# - Program slúži na výpočet dĺžky najdlhšieho súvislého bloku rovnakých znakov v reťazci a vypíše túto dĺžku.