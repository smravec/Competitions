a = int(input())
b = int(input())
c = []
e = 0 
for x in range(a):
    c.append(int(input()))
    
for x in range(int(len(c)) - 1):
    print(c[e] + b , end = " ")
    e = e + 1
print(c[e] + b)
