n = int(input())

raw_cisla = input()
input_cisla = list(map(int, raw_cisla.split()))

q = int(input())
otazky = []
for x in range(q):
    otazky.append(int(input()))

#n = 11
#input_cisla = [-10, -5, -3, 0, 1, 4, 5,6, 7, 14, 88]
#q = 6
#otazky = [2, 7, 5, -10 , 89, 6 ]
#spravny output je N, A, A, A, N, A

zaciatok = 0
koniec = len(input_cisla) - 1
stred = int((zaciatok + koniec) / 2)

#s-5 -3 s1 7m 88e

def najdi_cislo(hladane_cislo, zaciatok, koniec, stred):
    if zaciatok > koniec:
        return "N"
    elif hladane_cislo == input_cisla[stred]:
        return "A"
    elif hladane_cislo == input_cisla[zaciatok]:
        return "A"
    elif hladane_cislo == input_cisla[koniec]:
        return "A"

    else:
        if input_cisla[stred] < hladane_cislo:
            zaciatok = stred + 1
            stred = int((zaciatok + koniec) / 2)
            return najdi_cislo(hladane_cislo, zaciatok, koniec, stred)
        elif input_cisla[stred] > hladane_cislo:
            koniec = stred - 1 
            stred = int((zaciatok + koniec) / 2)
            return najdi_cislo(hladane_cislo, zaciatok, koniec, stred)
        else:
            return "N"
    

for x in otazky:
    #print(f"otazka: {x}")
    vyhladavanie1 = najdi_cislo(x, zaciatok, koniec, stred)
    vyhladavanie2 = najdi_cislo(x * -1, zaciatok, koniec, stred)
    if vyhladavanie1 == "A" or vyhladavanie2 == "A":
        print("A")
    else:
        print("N")
