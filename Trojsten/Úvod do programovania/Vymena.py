pocet_riadky , dlzka_riadky = input().split()
pocet_riadky , dlzka_riadky = [int(pocet_riadky) , int(dlzka_riadky)]

cisla1 = []

for x in range(pocet_riadky):
    cisla1.append([int(dlzka_riadky) for dlzka_riadky in input().split()])

#cisla1 = [[1, 2, 4, 5, 5], [1, 5, 6, 7, 3], [3, 5, 6, 7, 2]]
#pocet_riadky = 3
#dlzka_riadky = 5


a = 0
b = 0

for x in range(dlzka_riadky):
    a = 0

    for x in range(pocet_riadky):
        if a + 1 == pocet_riadky:
            print(cisla1[a][b])
            break
        
        print(cisla1[a][b] , end = " ")
        a = a + 1

    b = b + 1
    
        
        


