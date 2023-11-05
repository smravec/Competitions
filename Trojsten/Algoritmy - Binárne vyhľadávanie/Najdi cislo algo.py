pocet_cisel = int(input())

cisla = [int(x) for x in input().split()]

pocet_otazok = int(input())

otazky = []

for x in range(pocet_otazok):
    otazky.append(int(input()))

#pocet_cisel = 5
#cisla = [1 , 2, 8, 9, 15]
#pocet_otazok = 3 
#otazky = [2, 5, 15]


def binarne_vyhladavanie(cisla, zaciatok, koniec, hladane_cislo):
    if zaciatok > koniec:
        return -1

    stred = int((zaciatok + koniec) / 2)
    if cisla[stred] == hladane_cislo:
        return stred
    elif cisla[stred] > hladane_cislo:
        
        return binarne_vyhladavanie(cisla, zaciatok, stred - 1, hladane_cislo)
    elif cisla[stred] < hladane_cislo:

        return binarne_vyhladavanie(cisla, stred + 1, koniec, hladane_cislo)

    return - 1
pomocka = 0
for dlzka_otazok in range(pocet_otazok):
    print(binarne_vyhladavanie(cisla, 0, len(cisla) - 1, otazky[dlzka_otazok]))
    #print("pozicia:" + str(dlzka_otazok - 1))
    
        
    


    

    
