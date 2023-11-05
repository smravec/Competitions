pocet_cisel = int(input())

cisla = [int(x) for x in input().split()]

pocet_otazok = int(input())

otazky = []

for x in range(pocet_otazok):
    otazky.append(int(input()))


#pocet_cisel = 5
#cisla = 1, 2, 8, 9, 15
#pocet_otazok = 3
#otazky = 2, 5, 15


a = 0
b = 0
c = 0

for x in range(pocet_otazok ):
    
    for x in range(pocet_cisel):

        if cisla[a] == otazky[b]:
            print(a)
            break
        

        c = c + 1
        a = a + 1
        if c == pocet_cisel:
            print(-1)

    c = 0    
    b = b + 1
    a = 0
