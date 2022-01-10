import sys
from collections import deque
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
dy = (-1, 1, 0, 0)
dx = (0, 0, 1, -1)
mm = [0] * n
v_init = [0] * (k + 1)
for i in range(k + 1) :
    v_init[i] = []
for i in range(n) :
    mm[i] = list(map(int, input().split()))
s, ey, ex = map(int, input().split())
for i in range(n) :
    for j in range(n) :
        num = mm[i][j]
        if num == 0 : continue
        v_init[num].append((i, j))
dq = deque()
for i in range(1, k + 1) :
    for j in v_init[i] :
        dq.append(j)

for _ in range(s) :
    qsz = len(dq)
    while qsz > 0 :
        qsz -= 1
        y, x = dq.popleft()
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and mm[ny][nx] == 0 :
                mm[ny][nx] = mm[y][x]
                dq.append((ny, nx))
print(mm[ey - 1][ex - 1])

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
t, p, q = map(int, input().split())
p -= 1
q -= 1

mnd = 1e9
mnc = 1e9

def dist(x, y, a, b):
    return abs(x-a) + abs(y-b)

for i in range(n):
    for j in range(n):
        if a[i][j] > 0 and mnd > dist(i, j, p, q):
            mnd = dist(i, j, p, q)
            mnc = a[i][j]
        elif a[i][j] > 0 and mnd == dist(i, j, p, q) and mnc > a[i][j]:
            mnc = a[i][j]

if mnd <= t: print(mnc)
else: print(0)