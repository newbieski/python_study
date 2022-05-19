import sys

input = sys.stdin.readline

n = int(input())
INF = (10**9) * 400
sw = []
for _ in range(n) :
    sw.append(list(map(int, input().split())))
m = int(input())
dp = [INF for _ in range(m + 1)]
dp[0] = 0
for a,b in sw :
    if a == 1 : continue
    for i in range(m, 0, -1) :
        if i + a - 2 <= m : dp[i + a - 2] = min(dp[i + a - 2], dp[i] + b)
    if a - 1 <= m : dp[a - 1] = min(dp[a - 1], dp[0] + b)
if dp[m] == INF : dp[m] = -1
if m == 1 : dp[m] = 0
print(dp[m])