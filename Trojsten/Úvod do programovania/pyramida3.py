cislo = int(input())

#cisla pouzite na vypocet parne cislo
cislo2 = cislo - 2  // 2
cislo3 = cislo - (cislo - 2)

#cisla pouzite na vypocet neparne cislo
cislo4 = (cislo - 1)
cislo5 = (cislo * 2 - 1) - (cislo * 2 - 2)

#parne alebo neparne cislo
a = 0
if cislo // 2 - cislo / 2 == 0:
    a = a + 1
else:
    a = a + 2


    
#parne cislo
if a == 1:
    while cislo > 0:
        
        for i in range(cislo2):
            print("." , end = "" )
        for i in range(cislo3):
            print("*", end = "")
        for i in range(cislo2):
            print("." , end = "" )
        print("")
        
        cislo = cislo - 1
        cislo2 = cislo2 - 1
        cislo3 = cislo3 + 2
        
#neparne cislo
if a == 2:
    while cislo > 0:
        for i in range(cislo4):
            print("." , end = "" )
        for i in range(cislo5):
            print("*", end = "")
        for i in range(cislo4):
            print("." , end = "" )
        print("")

        cislo = cislo - 1
        cislo4 = cislo4 - 1
        cislo5 = cislo5 + 2
        
        
        
    
    
        



