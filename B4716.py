import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

def consumeA(a, k, c, sum) :
    tmp = min(a, k)
    return a - tmp, k -tmp, sum + tmp * c

def consumeB(b, k, d, sum) :
    tmp = min(b, k)
    return b - tmp, k - tmp, sum + tmp * d

while True :
    n, a, b = map(int, input().split())
    if n == 0 : break
    team = []
    for _ in range(n) :
        k, c, d = map(int, input().split())
        g = c - d
        if g > 0 : g = -g
        team.append((g, k, c, d))
    team.sort()
    ans = 0
    for g, k, c, d in team :
        if c < d :
            a, k, ans = consumeA(a, k, c, ans)
            b, k, ans = consumeB(b, k, d, ans)
        else :
            b, k, ans = consumeB(b, k, d, ans)
            a, k, ans = consumeA(a, k, c, ans)
    print(ans)


"""
while 1:
    n, a, b = map(int, input().split())
    if n == a == b == 0: break
    arr = sorted([[*map(int, input().split())]for _ in range(n)], key=lambda x: -abs(x[1]-x[2]))
    ans = 0
    for k, x, y in arr:
        if x <= y: val = min(k, a)
        else: val = k - min(k, b)
        ans += val * x + (k - val) * y
        a -= val
        b -= k - val
    print(ans)
"""