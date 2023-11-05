cislo = int(input())

cislo2 = (cislo - 1)
cislo3 = (cislo * 2 - 1) - (cislo * 2 - 2)


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

