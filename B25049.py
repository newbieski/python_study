import sys
sys.stdin=open("input.in", "r")
input=sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

def maxsub(a) :
    res, cur, mx = [], 0, 0
    for i in a :
        cur += i
        if cur < 0 : cur = 0
        mx = max(cur, mx)
        res.append(mx)
    return res

fw = maxsub(a)
rev = maxsub(a[::-1])[::-1]
ans = max(0, fw[n - 1], rev[0])
for i in range(n - 1) :
    ans = max(ans, fw[i]+rev[i + 1])
print(ans + sum(a))
