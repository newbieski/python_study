import sys
import math
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
MAXV = 4000 * 16
n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
def dist(a, b) :
    ax, ay = p[a]
    bx, by = p[b]
    dx, dy = ax - bx, ay - by
    return math.sqrt(dx * dx + dy * dy)
dp = []
for _ in range(1<<n) :
    dp.append([MAXV for _ in range(n)])
dp[1][0] = 0

for i in range(1<<n) :
    for j in range(n) :
        if dp[i][j] == MAXV : continue
        for k in range(n) :
            if i & (1<<k) : continue
            dp[i | 1<<k][k] = min(dp[i | 1<<k][k], dp[i][j] + dist(j, k))
ans = MAXV
for i in range(n) :
    ans = min(ans, dp[(1<<n) - 1][i] + dist(i, 0))
print(ans)