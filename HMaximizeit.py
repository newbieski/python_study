import sys
sys.stdin = open("input.in", "r")
l = []
ans = 0
k, m = map(int, input().split())
def brute(d, sum) :
    if d == k :
        global ans
        if ans < sum % m : ans = sum % m
    else :
        for i in l[d] :
            brute(d + 1, sum + i * i)

for _ in range(k) :
    a = list(map(int, input().split()))
    l.append(a[1:])

brute(0, 0)
print(ans)
