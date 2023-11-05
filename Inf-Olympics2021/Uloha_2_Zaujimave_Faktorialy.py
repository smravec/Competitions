a = int(input())
b = int(input())

def zisti_kolko_najviac_mocnin_5_ma_cislo(cislo):
    momentalna_mocnina_5 = 5
    kolko_ma_mocnin_5 = 0

    while cislo >= momentalna_mocnina_5:
        kolko_ma_mocnin_5 += 1
        momentalna_mocnina_5 *= 5

    return kolko_ma_mocnin_5

def zisti_kolko_nul_ma_faktorial_na_konci(cislo, kolko_ma_mocnin_5):
    kolko_nul = 0
    momentalna_mocnina_5 = 5

    for _ in range(kolko_ma_mocnin_5):
        kolko_nul += cislo // momentalna_mocnina_5
        momentalna_mocnina_5 *= 5

    return kolko_nul

pocet_nul = 0
while a <= b:

    if a >= 5:
        pocet_nul += zisti_kolko_nul_ma_faktorial_na_konci(a, zisti_kolko_najviac_mocnin_5_ma_cislo(a))
        
    a += 1
print(pocet_nul)