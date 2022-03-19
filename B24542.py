import sys
sys.stdin = open("input.in", "r")

input = sys.stdin.readline
n, m = map(int, input().split())
sys.setrecursionlimit(n + 10)
p = list(range(n + 1))
sz = [1 for _ in range(n + 1)]

def find(a) :
    global p
    if a == p[a] : return a
    p[a] = find(p[a])
    return p[a]

def union(a, b) :
    global p, sz
    a, b = find(a), find(b)
    if a != b :
        p[a] = b
        sz[b] += sz[a]

for _ in range(m) :
    a, b = map(int, input().split())
    union(a, b)

ans = 1
MOD = 10**9+7
vt = set()
for i in range(1, n + 1) :
    a = find(i)
    if a not in vt :
        vt.add(a)
        ans *= sz[a]
        ans %= MOD

print(ans)
