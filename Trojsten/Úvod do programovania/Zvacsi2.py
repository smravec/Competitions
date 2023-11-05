a = int(input())

b = list(map (int, input().split()))
c = int(input())
e = 0
for x in range(a - 1):
    print(b[e] + c , end = " ")
    e = e + 1
    
print(b[e] + c )



