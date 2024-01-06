print(1^16, 10^16, 17^16)

import sys
sys.stdin=open("input.in", "r")
input=sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))
ans=[]
for _ in range(n) :
    ans.append([0 for _ in range(n)])
for l in range(n) :
    x = [0 for _ in range(512)]
    for r in range(l, n) :
        y = x.copy()
        y[a[r]] = max(y[a[r]], 1)
        for i in range(512) :
            if x[i] == 0 : continue
            tmp = i ^ a[r]
            y[tmp] = max(y[tmp], x[i] + 1)
        for i in range(512) :
            if y[i] > 0 :
                ans[l][r] = max(ans[l][r], i + y[i])
        x = y

for _ in range(int(input())) :
    l,r=map(int,input().split())
    l, r = l - 1 , r - 1
    print(ans[l][r])