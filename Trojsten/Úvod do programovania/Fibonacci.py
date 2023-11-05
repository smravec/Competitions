a = int(input())

b = 0
c = 1
d = [0 , 1]
e = 0
for x in range(28):
    f = d[b] + d[c]
    d.append(f)
    b = b + 1
    c = c + 1
    

for x in range(a - 1):
    print(d[e] , end = " ")

    e = e + 1
print(d[e])    
    
