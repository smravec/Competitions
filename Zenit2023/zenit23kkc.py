n = int(input())
tricka = input().split(" ")

counter = {}

for item in tricka:
    if item in counter:
        counter[item] =  counter[item] + 1
    else:
        counter[item] = 1

if len(counter) > 1: 
    max1 = 0
    max2 = -1

    for x in counter:
        if counter[x] >= max1: 
            max2 = max1
            max1 = counter[x]

    print(max1 + max2)
else:
    print(counter[counter.keys()[0]])