import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
sys.setrecursionlimit(n + m + 100)
cache = []
MAX = 1000 * 50 * 50 * 50 * 50 * 50
for _ in range(n + 1) :
    p = []
    for _ in range(m + 1) :
        q = []
        for _ in range(n + 1) :
            q.append([0 for _ in range(m + 1)])
        p.append(q)
    cache.append(p)

g = []
g.append([0 for _ in range(m + 1)])
for i in range(1, n + 1) :
    a = [0]
    a.extend(list(map(int, input().split())))
    g.append(a)
    sum = 0
    for j in range(1, m + 1) :
        sum += g[i][j]
        g[i][j] = sum + g[i - 1][j]

def subsum(ay, ax, by, bx) :
    return g[by][bx] - g[by][ax - 1] - g[ay - 1][bx] + g[ay - 1][ax - 1]

def dp(ay, ax, by, bx) :
    if cache[ay][ax][by][bx] : return cache[ay][ax][by][bx]
    if ay == by and ax == bx :        
        return 0
    res = MAX
    for i in range(ay, by) :
        res = min(res, dp(ay, ax, i, bx) + dp(i + 1, ax, by, bx))
    for i in range(ax, bx) :
        res = min(res, dp(ay, ax, by, i) + dp(ay, i + 1, by, bx))
    res += subsum(ay, ax, by, bx)
    cache[ay][ax][by][bx] = res
    return res

print(dp(1, 1, n, m))