r,c = input().split()
r,c = int(r), int(c)

mena = input().split(" ")

riadky = []

for riadok in range(r):
    input1 = input()
    input2 = [*input1]
    riadky.append(input2)

for index,item in enumerate(riadky):
    for index1,char in enumerate(item):
        if char != ".":
            riadky[index][index1] = mena[int(char) - 1]


for item in riadky:
    output = ""
    for char in item:
        output = f"{output}{char}"
    print(output)