import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
dp = []
for _ in range(n + 1) :
    tmp = []
    for _ in range(n + 1) :
        tmp.append([-1, -1])
    dp.append(tmp)
dp[0][0][0] = 0
for _ in range(n) :
    p, q, r, s = map(int, input().split())
    for i in range(n, -1, -1) :
        for j in range(n, -1, -1) :
            for k in range(1, -1, -1) :
                if dp[i][j][k] == -1 : continue
                dp[i][j + 1][0] = max(dp[i][j + 1][0], max(p, q) + dp[i][j][k])
                if k == 0 :
                    dp[i][j][1] = dp[i][j][k] + r
                dp[i + 1][j][0] = max(dp[i + 1][j][0], s + dp[i][j][k])
                
ans = 0
for i in range(0, a + 1) :
    for j in range(b, n + 1) :
        ans = max(ans, dp[i][j][0])
        ans = max(ans, dp[i][j][1])
print(ans)