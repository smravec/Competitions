a = int(input())
b = [int(a) for a in input().split()]
e = int(input())

c = []
d = 0


for x in range(a):
    if b[d] < e:
        c.append(b[d])
    d = d + 1 

d = 0
f = 0

for x in range(len(c)):
    f = f + c[d]
    d = d + 1
print(f)
    
    


     
