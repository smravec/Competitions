dlzka = int(input())

cisla1 = []
for x in range(dlzka):
    cisla1.append([int(dlzka) for dlzka in input().split()])

#cisla1 = [[2, 1, 3], [3, 2, 5], [7, 1, 2]]
#dlzka = 3

a = 0
b = dlzka - 1

for x in range(dlzka):

    for x in range(dlzka):
        if a + 1 == dlzka:
            print(cisla1[a][b])
            break
        
        print(cisla1[a][b] , end = " ")
        a = a + 1
        
    b = b - 1
    a = 0
