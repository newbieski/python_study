import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
INF = 10**9

n,a,b,e = map(int, input().split())
ai = [0]
for _ in range(n) :
    ai.append(int(input()))
for _ in range(n) :
    ai.append(0)

for i in range(1, 2 * n + 1) :
    ai[i] += ai[i - 1]

def check(buf, k) :
    cur = 0
    for i in buf :
        cur += k        
        if cur < i - e + 1 : return False
    return True

def findk(buf) :
    l, r, res = 1, sum(buf), sum(buf)
    while l <= r :
        mid = (l + r) // 2
        if check(buf, mid) :
            res = min(res, mid)
            r = mid - 1
        else : l = mid + 1
    return res

def sol() :
    #print(*ai)
    if ai[n] < e : return -b * INF
    res = a * (ai[n] - e + 1) - b * INF
    for t in range(1, n + 1) :
        buf = []
        for i in range(t, n + t, t) :
            buf.append(ai[i])
        k = findk(buf)
        #print(t, buf, k, a*k-b*t)
        res = min(res, a*k-b*t)
    return res

print(sol())
