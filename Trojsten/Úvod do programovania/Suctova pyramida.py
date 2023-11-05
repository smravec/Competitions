pocet_cisel = int(input())

cisla1 = [int(a) for a in input().split()]


cisla2 = []
a = 0
b = 1
c = 0

for x in range(pocet_cisel - 1):

    
    
    for x in range(len(cisla1) - 1):
        cisla2.append(cisla1[a] + cisla1[b])
        a = a + 1
        b = b + 1

    for x in range(len(cisla2) - 1):
        print(cisla2[c] , end = " ")

        c = c + 1
    print(cisla2[c])

    
    cisla1 = cisla2
    cisla2 = []
    a = 0
    b = 1
    c = 0





    
    
    


    
