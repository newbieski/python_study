mod = 1000000007
dp = [[0] * 3 for _ in range(1516)]
dp[0][0] = 1
for i in range(1, 1516) :
    for j in range(3) :
        dp[i][(j + 1) % 3] += dp[i - 1][j]
        dp[i][(j + 1) % 3] %= mod
        dp[i][(j + 5) % 3] += dp[i - 1][j]
        dp[i][(j + 5) % 3] %= mod

n = int(input())
print(dp[n - 1][1])

n = int(input())-1
print(int((2**n-(-1)**n)//3) % 1000000007)