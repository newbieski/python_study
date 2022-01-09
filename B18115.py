import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dq = deque()
i, j = n - 1, 1
while i >= 0 :
    if a[i] == 1 :
        dq.appendleft(j)
    elif a[i] == 2 :
        tmp = dq.popleft()
        dq.appendleft(j)
        dq.appendleft(tmp)
    else :
        dq.append(j)
    i -= 1
    j += 1
print(*dq)

from collections import deque
n=int(input())
r=deque(input().split())
a=deque(range(1,n+1))
b=deque()
while r:
 t=r.pop();l=a.popleft()
 if t=='1':b.appendleft(l)
 elif t=='2':b.insert(1,l)
 else:b.append(l)
print(*b)
