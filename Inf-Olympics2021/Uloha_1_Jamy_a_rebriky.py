celkove_policka = int(input()) - 1
jamy_a_rebriky_str = input()

#convert jamy_a_rebriky_str to int list
jamy_a_rebriky = list(map(int, jamy_a_rebriky_str.split()))

#vars
momentalne_policko = 0
tahy = 0

def viem_sa_na_toto_policko_dostat(index_policka_na_ktore_sa_chcem_dostat, index_kde_zacinam):
    while index_kde_zacinam != index_policka_na_ktore_sa_chcem_dostat:
        
        najvacsi_mozny_pohyb_z_policka = -1
        
        if index_kde_zacinam + 6 > index_policka_na_ktore_sa_chcem_dostat:
            kolko_policok_sa_mozem_posunut1 = index_policka_na_ktore_sa_chcem_dostat - index_kde_zacinam
        else:
            kolko_policok_sa_mozem_posunut1 = 6

        for hod_kockou in range(kolko_policok_sa_mozem_posunut1):
            hod_kockou = hod_kockou + 1
            
            #checks if policko after hod kockou is - 1
            if jamy_a_rebriky[hod_kockou + index_kde_zacinam] != -1:
                
                #checks if ladder is ending with -1
                if jamy_a_rebriky[jamy_a_rebriky[hod_kockou + index_kde_zacinam] + index_kde_zacinam + hod_kockou] != -1:
                

                    #checks if throw with this number is better than the previous one
                    if jamy_a_rebriky[hod_kockou + index_kde_zacinam] + hod_kockou > najvacsi_mozny_pohyb_z_policka:
                        najvacsi_mozny_pohyb_z_policka = jamy_a_rebriky[hod_kockou + index_kde_zacinam] + hod_kockou
        if najvacsi_mozny_pohyb_z_policka == -1:
            return False

        else: index_kde_zacinam += najvacsi_mozny_pohyb_z_policka
    return True

if jamy_a_rebriky[-1] == -1:
    print(-1)
else:
    #main game cyklus
    while momentalne_policko != celkove_policka:

        tahy += 1
        
        if momentalne_policko + 6 <= celkove_policka :
            kolko_policok_sa_mozem_posunut = 6
        else:
            kolko_policok_sa_mozem_posunut = celkove_policka - momentalne_policko
        
        najvacsi_mozny_pohyb_z_policka = -1

        for hod_kockou in range(kolko_policok_sa_mozem_posunut):
            hod_kockou = hod_kockou + 1
            
            #checks if policko after hod kockou is - 1
            if jamy_a_rebriky[hod_kockou + momentalne_policko] != -1:
                
                #checks if ladder is ending with -1
                if jamy_a_rebriky[jamy_a_rebriky[hod_kockou + momentalne_policko] + momentalne_policko + hod_kockou] != -1:
                

                    #checks if throw with this number is better than the previous one
                    if jamy_a_rebriky[hod_kockou + momentalne_policko] + hod_kockou > najvacsi_mozny_pohyb_z_policka:
                        najvacsi_mozny_pohyb_z_policka = jamy_a_rebriky[hod_kockou + momentalne_policko] + hod_kockou
                        hod_kockou1 = hod_kockou

        if najvacsi_mozny_pohyb_z_policka == -1:
            momentalne_policko = celkove_policka
            tahy = -1
        else:
            #checks if is using ladder
            if jamy_a_rebriky[momentalne_policko + najvacsi_mozny_pohyb_z_policka] > 0:
                
                index_prveho_preskoceneho_policka = momentalne_policko + hod_kockou1 + 1
                index_posledneho_preskoceneho_policka = momentalne_policko + najvacsi_mozny_pohyb_z_policka 
                ktore_policko_checkujem = index_prveho_preskoceneho_policka
                najvacsie_policko = 0
                
                while ktore_policko_checkujem <= index_posledneho_preskoceneho_policka:
                    #checks if any ladder is more efficient to use and if u can get to this policko
                    if jamy_a_rebriky[ktore_policko_checkujem] > najvacsi_mozny_pohyb_z_policka and viem_sa_na_toto_policko_dostat(ktore_policko_checkujem, momentalne_policko) and jamy_a_rebriky[ktore_policko_checkujem] > jamy_a_rebriky[najvacsie_policko]:
                        najvacsie_policko = ktore_policko_checkujem
                    ktore_policko_checkujem += 1
                
                if najvacsie_policko != 0:
                    najvacsi_mozny_pohyb_z_policka = 0
                    for x in range(kolko_policok_sa_mozem_posunut):
                        x = x + 1
                        if jamy_a_rebriky[x + momentalne_policko] != -1:
                
                            if jamy_a_rebriky[jamy_a_rebriky[x + momentalne_policko] + momentalne_policko + x] != -1:
                                if momentalne_policko + x + jamy_a_rebriky[momentalne_policko + x] > najvacsi_mozny_pohyb_z_policka and momentalne_policko + x + jamy_a_rebriky[momentalne_policko + x] < najvacsie_policko:
                                    najvacsi_mozny_pohyb_z_policka = momentalne_policko + x + jamy_a_rebriky[momentalne_policko + x]

                    

            momentalne_policko += najvacsi_mozny_pohyb_z_policka        

    print(tahy)
