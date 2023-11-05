a ,b = input().split()
a, b = [int(a), int(b)]
c = [int(a) for a in input().split()]
f = False
e = 1
d = 1
g = 0
for x in range(a - 1): 
    for x in range(a - d):
        if c[g] - c[e] == b or  c[g] - c[e] == -b  :
            f = True
        e = e + 1
    e = g + 1     
    d = d + 1
    g = g + 1

e = len(c) - 2
for x in range(a - 1):
    if c[a - 1] - c[e] == b or c[a - 1] - c[e] == -b:
        f = True
    e = e - 1
 


if f == True:
    print("Ano")
else:
    print("Nie")
    


