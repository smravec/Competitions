pocet_cisel = int(input())

cisla = [int(x) for x in input().split()]

pocet_otazok = int(input())

otazky = []

for x in range(pocet_otazok):
    otazky.append(int(input()))

a = 0

for x in range(len(otazky)):
    
    if  otazky[a] in cisla:
        print(cisla.index(otazky[a]))

    else:
        print( -1 )
        
    a = a + 1
    
