import sys

input = sys.stdin.readline
n = int(input())
a = []
csum = []
ans = -(10**9)*18*18
for _ in range(n) :
    a.append([*map(int, input().split())])

for x in zip(*a) :
    csum.append(sum(x))

for x in range(1<<n) :
    tmpsum = [0] * n
    for r in range(n) :
        if x & (1<<r) :
            for i in range(n) :
                tmpsum[i] += a[r][i]
    tmp = 0
    for i in range(n) :
        tmp += min(csum[i] - tmpsum[i], tmpsum[i])
    ans = max(ans, tmp)
print(ans)
