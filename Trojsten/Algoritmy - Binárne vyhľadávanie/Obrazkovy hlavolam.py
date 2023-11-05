#Notes

n, k = input().split()
n, k = int(n), int(k)

#n = 4
#input_cisla = [4, 1, 2 , 6, 3]
input_cisla = []
for x in range(k):
    input_cisla.append(int(input()))

max_pocet_rovnakych_riadkov = 0

if max(input_cisla) >= n:
    max_pocet_rovnakych_riadkov = n
else:
    max_pocet_rovnakych_riadkov = max(input_cisla)

zaciatok = 1
koniec = max_pocet_rovnakych_riadkov
stred = int((zaciatok + koniec) / 2)

def zisti_kolko_viem_poskladat_pri_urcitom_cisle(cislo_pri_ktorom_skladam):
    kolko_rovnakych_riadkov_viem_poskladat = 0
    for x in input_cisla:
        kolko_rovnakych_riadkov_viem_poskladat = kolko_rovnakych_riadkov_viem_poskladat + int(x / cislo_pri_ktorom_skladam)

    if kolko_rovnakych_riadkov_viem_poskladat >= n :
        return True
    else:
        return False


def zisti_kolko_najviac_moze_byt_rovnakych(zaciatok, koniec, stred):
    viem_poskladat_dostatocne_vela_riadkov_pri_strede = zisti_kolko_viem_poskladat_pri_urcitom_cisle(stred)
    viem_poskladat_dostatocne_vela_riadkov_pri_strede_plus_1 = zisti_kolko_viem_poskladat_pri_urcitom_cisle(stred + 1)
    viem_poskladat_dostatocne_vela_riadkov_pri_konci = zisti_kolko_viem_poskladat_pri_urcitom_cisle(koniec)
    viem_poskladat_dostatocne_vela_riadkov_pri_zaciatku = zisti_kolko_viem_poskladat_pri_urcitom_cisle(zaciatok)
    #viem_poskladat_dostatocne_vela_riadkov_pri_zaciatku_plus_1 = zisti_kolko_viem_poskladat_pri_urcitom_cisle(zaciatok + 1)

    if viem_poskladat_dostatocne_vela_riadkov_pri_zaciatku == True and stred - 1 == zaciatok and viem_poskladat_dostatocne_vela_riadkov_pri_strede == False:
        print(zaciatok)
    
    elif viem_poskladat_dostatocne_vela_riadkov_pri_konci == True:
        print(koniec)

    elif viem_poskladat_dostatocne_vela_riadkov_pri_strede == True and viem_poskladat_dostatocne_vela_riadkov_pri_strede_plus_1 == False:
        print(stred)

    else:

        if viem_poskladat_dostatocne_vela_riadkov_pri_strede_plus_1 == True:
            zaciatok = stred
            stred = int((zaciatok + koniec) / 2)
            zisti_kolko_najviac_moze_byt_rovnakych(zaciatok, koniec, stred)
        
        else:
            koniec = stred
            stred = int((zaciatok + koniec) / 2)
            zisti_kolko_najviac_moze_byt_rovnakych(zaciatok, koniec, stred)     
        
zisti_kolko_najviac_moze_byt_rovnakych(zaciatok,koniec,stred)
    







    

