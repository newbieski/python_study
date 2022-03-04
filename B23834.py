import sys
import collections
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0]
b = [0]
a.extend(list(map(int, input().split())))
b.extend(list(map(int, input().split())))
#print(n, m)
#print("a : ", a)
#print("b : ", b)
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1) : a[i] += a[i - 1]
def subsum(l, r) : return a[r] - a[l - 1]

dq = collections.deque()
for i in range(1, n + 1) :
    if len(dq) > 0 and dq[0] == i - m :
        dq.popleft()
    while len(dq) > 0 :
        tmp = dq[len(dq) - 1]        
        val = dp[tmp - 1] - subsum(tmp, tmp) + subsum(tmp + 1, i)
        if val <= dp[i - 1] - subsum(i, i) : dq.pop()
        else : break
    dq.append(i)
    tmp = dq[0]
    if i < m :
        dp[i] = subsum(1, i)
    else :
        dp[i] = dp[tmp - 1] - subsum(tmp, tmp) + subsum(tmp + 1, i)


ans = dp[n]
if n >= m :
    ans = max(ans, subsum(1, m) + b[m])
    for i in range(m + 1, n + 1) :
        tmp = i - m
        val = subsum(tmp + 1, i) - subsum(tmp, tmp) + dp[tmp - 1] + b[i]
        ans = max(ans, val)
print(ans)

import sys
from collections import deque
dq = deque()
dq.append(0)
INF = float('inf')
s, ans = [0], -1
n, m = map(int, sys.stdin.readline().split())
a = [0] + list(map(int, sys.stdin.readline().split()))
b = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):  s.append(s[-1] + a[i])
for i in range(1, n + 1):
    f = dq[0]
    dp[i] = dp[f] + s[i - 1] - s[f] - a[i]
    if i - f >= m:    dq.popleft()
    while dq:
        if dp[i] < dp[dq[-1]] + s[i] - s[dq[-1]]:    break
        dq.pop()
    dq.append(i)
for i in range(n + 1):
    if i + m <= n:    ans = max(ans, dp[i] + s[i + m] - s[i] + b[i + m])
    else:    ans = max(ans, dp[i] + s[n] - s[i])
print(ans)

import sys
from collections import deque
ip=sys.stdin.readline
d=deque()
n,m=map(int,ip().split())
x=list(map(int,ip().split()))
y=list(map(int,ip().split()))
f=[0]*(n+5)
for i in range(n):
  f[i]=f[i-1]+x[i]
a=0
b=[0]*(n+5)
ans=-float('inf')
d.append((0,-1))
for i in range(n):
  if i+1>=m:
    ans=max(ans,b[i-m]+y[i]+f[i]-f[i-m])
  b[i]=max(b[i-1],a)-x[i]
  while d and d[0][1]<=i-m:
    d.popleft()
  a=d[0][0]+f[i]-f[d[0][1]]
  while d:
    if b[i]<d[-1][0]+f[i]-f[d[-1][1]]:
      break
    d.pop()
  d.append((b[i],i))
print(max(ans,max(a,b[n-1])))