a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a > b:
    najvacsie = a
if b > a :
    najvacsie = b
if najvacsie < c:
    najvacsie = c
if najvacsie < d :
    najvacsie = d
if najvacsie < e:
    najvacsie = e
print((a + b + c + d + e ) - najvacsie)






