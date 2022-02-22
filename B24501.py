import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
esm = ['*'*(m + 1)]
MOD = 10**9+7
for _ in range(n) :
    esm.append("*" + input().strip())

e = []
e.append([0 for _ in range(m + 1)])
for i in range(1, n + 1) :
    sum = 0
    tmp = [0]
    for j in range(1, m + 1) :
        if esm[i][j] == 'E' : sum += 1
        tmp.append(e[i - 1][j] + sum)
    e.append(tmp)

s = []
s.append([0 for _ in range(m + 1)])
for i in range(1, n + 1) :
    sum = 0
    tmp = [0]
    for j in range(1, m + 1) :
        if esm[i][j] == 'S' : sum += e[i][j]
        tmp.append((s[i - 1][j] + sum) % MOD)
    s.append(tmp)

ans = 0
for i in range(1, n + 1) :
    sum = 0
    for j in range(1, m + 1) :
        if esm[i][j] == 'M' :
            ans += s[i][j]
            ans %= MOD
print(ans)