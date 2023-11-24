n = int(input())
cisla = (list(map(int,input().split())))

sucin = 1

for x in cisla:
    sucin = sucin * x

vysledky = ""

for index,x in enumerate(cisla):
    if index == 0:
        vysledky = f"{str(sucin // x)}"
    else:
        vysledky = f"{vysledky} {str(sucin // x)}"

print(vysledky)