import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
sys.setrecursionlimit(110000)
n,m=map(int, input().split())
ai, bi = [0], [0]
ai.extend(list(map(int, input().split())))
bi.extend(list(map(int, input().split())))
p = [i for i in range(n + 1)]
cnt = [1 for i in range(n + 1)]
ans = 0

def find(x) :
    if x == p[x] :
        return x
    p[x] = find(p[x])
    return p[x]
def union(x, y) :
    global ans
    x, y = find(x), find(y)
    if x == y :
        return
    if ai[x] < bi[x] :
        ans -= cnt[x]
    if ai[y] < bi[y] :
        ans -= cnt[y]
    p[x] = y
    ai[y] += ai[x]
    bi[y] += bi[x]
    cnt[y] += cnt[x]
    if ai[y] < bi[y] :
        ans += cnt[y]

for i in range(1, n + 1) :
    if ai[i] < bi[i] :
        ans += 1
for _ in range(m) :
    qr = list(map(int, input().split()))
    if qr[0] == 2 :
        print(ans)
    else :
        x,y=qr[1:]
        union(x,y)
