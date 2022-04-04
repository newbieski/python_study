import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
mbtis = []
for a in "EI" :
    for b in "NS" :
        for c in "FT" :
            for d in "PJ" :
                mbtis.append(a+b+c+d)
n,m = map(int, input().split())
w = []
for _ in range(n) :
    w.append(input().strip())
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
ans = 0

def calc(y, x, d) :
    s = w[y][x]
    for i in range(3) :
        y += dy[d]
        x += dx[d]
        if 0 <= y < n and 0 <= x < m :
            s += w[y][x]
        else : return 0
    if s in mbtis : return 1
    return 0
for i in range(n) :
    for j in range(m) :
        for d in range(8) :
            ans += calc(i, j, d)
print(ans)
