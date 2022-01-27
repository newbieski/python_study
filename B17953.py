import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
v = []
for _ in range(m) :
    v.append(list(map(int, input().split())))

dp = [v[i][0] for i in range(m)]
ndp = [0] * m
for i in range(1, n) :
    for j in range(m) : ndp[j] = 0
    for j in range(m) :
        for k in range(m) :
            val = v[j][i]
            if j == k : val //= 2
            ndp[j] = max(ndp[j], dp[k] + val)
    tmp = dp
    dp = ndp
    ndp = tmp

print(max(dp))


import sys
N, M = map(int, input().split())
dp = [[0 for _ in range(N)] for _ in range(M)]
board = []

def process(curr, N, M):
    val = 0
    for i in range(M):
        if i==curr:
            continue
        else:
            val = max(val, dp[i][N])
    return val

for i in range(M):
    tmp = []
    for j, elem in enumerate(list(map(int, sys.stdin.readline().split()))):
        tmp.append(elem)
        if j==0:
            dp[i][0] = elem
    board.append(tmp)

for i in range(1, N):
    for j in range(M):
        dp[j][i] = max(dp[j][i-1]+board[j][i]//2, process(j, i-1, M)+board[j][i])

ans = 0
for i in range(M):
    ans = max(ans, dp[i][-1])
print(ans)