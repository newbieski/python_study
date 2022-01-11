import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
a = []
yx = []
vt = [[0] * m for _ in range(n)]
ans = -50000

def check(y, x) :
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    for i in range(4) :
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and vt[ny][nx] : return False
    return True

def brute(s, d, sum) :
    if d == k :
        global ans
        ans = max(ans, sum)
        return
    for i in range(s, n * m) :
        y, x = yx[i]
        if check(y, x) :
            vt[y][x] = 1
            brute(i + 1, d + 1, sum + a[y][x])
            vt[y][x] = 0

for i in range(n) :
    a.append(list(map(int, input().split())))
    for j in range(m) :
        yx.append((i, j))
brute(0, 0, 0)
print(ans)