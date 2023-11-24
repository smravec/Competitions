n,s = input().split()
n,s = int(n),int(s)

M = 10**9 + 7

dp = [[0 for _ in range(s+1)] for _ in range(s+1)]

dp[0][0] = 1  

for i in range(1, s+1):
    for j in range(1, s+1):
        for k in range(1, n+1):
            
            if j - k >= 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % M

vysledok = 0
for i in range(1, s+1):
    vysledok = (vysledok + dp[i][s]) % M

print(vysledok)