import random
#Notes
#1. Ak je sucet vsetkych cukrikov ktore si deti zasluzia menej ako celkovy pocet cukrikov tak return Nic nedostanete

#Example 5 deti 34 cukrikov na rozdanie
#9 8 9 9 4
# min 1 - max 1 spolu v rozmedzi 5
# min 1 - max 2  spolu v rozmedzi 5 - 10
# min 1 - max 3 spolu v rozmedzi 5 - 15
# min 1 - max 4 spolu v rozmedzi 5 - 20
# min 1 - max 5 spolu v rozmedzi 5 - 24
# min 1 - max 6 spolu v rozmedzi 5 - 28
# min 1 - max 7 spolu v rozmedzi 5 - 32
# min 1 - max 8 spolu v rozmedzi 5 - 36
# max pocet moznych cukrikov je teraz vacsi ako 34 funkcia konci returnuje 8
# na zistenie r treba algo bin vyhladavanie 
# zaciname s 2 cislami 1 az 9 (v tomto pripade) start = 1 end = 9 r = 4
# ak je max sucet cisiel pri r 4 vacsi ako 34 tak end bude 15
# inak start bude 24 , dalej r je 32 a end ostava
# ak je max sucet pri r vacsi ako 34 tak end bude 28
# inak ak je mensi ako 34 tak start bude 36 a end 39 r bude 36
# PROBLEM END SA NEPOSUVA TREBA NEJAKO VYRIESIT 
#  
# 1  2  3  4  5  6  7  8  9 10
# s5 10 15m 20 24e 28 32 36 39e

pocet_ludi, pocet_cukrikov = input().split()
#pocet_ludi, pocet_cukrikov = 1000 ,1000000000

raw_cisla = input()
kolko_si_zasluzi = list(map(int, raw_cisla.split()))
#kolko_si_zasluzi = []
#for x in range(pocet_ludi):
    #kolko_si_zasluzi.append(random.randint(1,10000000))
sucet_cukrikov_ktore_si_deti_zasluzia = 0
for x in kolko_si_zasluzi:
    sucet_cukrikov_ktore_si_deti_zasluzia = sucet_cukrikov_ktore_si_deti_zasluzia + x

def zisti_kolko_rozda_pri_tomto_max_rozmedzi(max_cislo):
    kolko_rozda = 0
    for x in kolko_si_zasluzi:
        if x > max_cislo:
            kolko_rozda = kolko_rozda + max_cislo
        else:
            kolko_rozda = kolko_rozda + x

    return kolko_rozda
#trash aby program fungoval ignore
pocet_ludi = int(pocet_ludi)
pocet_cukrikov = int(pocet_cukrikov)
zaciatok = 1
koniec = max(kolko_si_zasluzi)
stred = int((zaciatok + koniec) / 2)

def zisti_cislo_r(zaciatok, koniec, stred):

    naslo_sa_cislo = False
    zaciatok_kolko_cukrikov_rozda = zisti_kolko_rozda_pri_tomto_max_rozmedzi(zaciatok)
    zaciatok_plus1_kolko_cukrikov_rozda = zisti_kolko_rozda_pri_tomto_max_rozmedzi(zaciatok + 1)
    koniec_kolko_cukrikov_rozda = zisti_kolko_rozda_pri_tomto_max_rozmedzi(koniec)
    koniec_minus1_kolko_cukrikov_rozda = zisti_kolko_rozda_pri_tomto_max_rozmedzi(koniec - 1)
    stred_kolko_cukrikov_rozda = zisti_kolko_rozda_pri_tomto_max_rozmedzi(stred)
    stred_plus1_kolko_cukrikov_rozda = zisti_kolko_rozda_pri_tomto_max_rozmedzi(stred + 1)
    stred_minus1_kolko_cukrikov_rozda = zisti_kolko_rozda_pri_tomto_max_rozmedzi(stred - 1)
    
    #Check ci zaciatok, koniec ,stred alebo stred plus 1 vyhovuje
    if zaciatok_kolko_cukrikov_rozda >= pocet_cukrikov:
        naslo_sa_cislo = True
        print(zaciatok)

    elif koniec_kolko_cukrikov_rozda >= pocet_cukrikov and koniec_minus1_kolko_cukrikov_rozda < pocet_cukrikov:
        naslo_sa_cislo = True
        print(koniec)

    elif stred_kolko_cukrikov_rozda >= pocet_cukrikov and stred_minus1_kolko_cukrikov_rozda < pocet_cukrikov:
        naslo_sa_cislo = True
        print(stred)

    elif stred_plus1_kolko_cukrikov_rozda >= pocet_cukrikov and stred_kolko_cukrikov_rozda < pocet_cukrikov:
        naslo_sa_cislo = True
        print(stred + 1)


    #Zisti na ktoru stranu sa ma zaciatok alebo koniec posunut
    if naslo_sa_cislo == False:
        if stred_kolko_cukrikov_rozda < pocet_cukrikov:
            zaciatok = stred
            stred  = int((zaciatok + koniec) / 2)
            zisti_cislo_r(zaciatok, koniec, stred)

        elif stred_kolko_cukrikov_rozda >= pocet_cukrikov:
            koniec = stred
            stred = int((zaciatok + koniec) / 2)
            zisti_cislo_r(zaciatok, koniec, stred)

if sucet_cukrikov_ktore_si_deti_zasluzia < pocet_cukrikov:
    print("Nic nedostanete")

else:
    zisti_cislo_r(zaciatok, koniec, stred)