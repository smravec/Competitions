#!/usr/bin/python

import string

ulica = str(input())

min_pocet_metrov = 0 
arr_cakajuci_zakaznici = [(0) for _ in range(26)]
kolko_m_za_krok = 0

for char in reversed(ulica):
    min_pocet_metrov += kolko_m_za_krok
    if char == char.upper():

        if arr_cakajuci_zakaznici[string.ascii_uppercase.index(char)] > 0:
            arr_cakajuci_zakaznici[string.ascii_uppercase.index(char)] -= 1
            kolko_m_za_krok -= 1
    else:
        arr_cakajuci_zakaznici[string.ascii_lowercase.index(char)] += 1
        kolko_m_za_krok += 1

print(min_pocet_metrov)
