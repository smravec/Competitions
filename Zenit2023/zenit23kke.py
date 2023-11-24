n, usek = input().split()
n , usek = int(n), int(usek)
cisla = (list(map(int,input().split())))

vysledok = f"{max(cisla[0:usek])}"

index = 1
while usek + index <= len(cisla):
    vysledok = f"{vysledok} {max(cisla[index:usek + index])}"
    index += 1

print(vysledok)