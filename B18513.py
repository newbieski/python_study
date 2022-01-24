import sys
import queue
import collections
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
pq = queue.PriorityQueue()
a = list(map(int, input().split()))
ans = 0
vt = collections.defaultdict(int)
for x in a :
    pq.put((1, x, x - 1))
    pq.put((1, x, x + 1))
    #vt.setdefault(x, 0)
    vt[x] = 1

while k > 0 :
    tmp = pq.get()
    #vt.setdefault(tmp[2], 0)
    if vt[tmp[2]] == 0:
        vt[tmp[2]] = 1
        ans += tmp[0]
        k -= 1
    
    if tmp[1] < tmp[2] :
        if vt[tmp[2] + 1] == 0 : pq.put((tmp[0] + 1, tmp[1], tmp[2] + 1))
    else :
        if vt[tmp[2] - 1] == 0 : pq.put((tmp[0] + 1, tmp[1], tmp[2] - 1))
print(ans)



from collections import deque
n, k = map(int,input().split())
well = list(map(int,input().split()))
dist = dict(zip(well, [0]*n))
Q = deque(well)
while len(dist) < n+k:
    p = Q.popleft()
    for q in p-1,p+1:
        if q in dist: continue
        dist[q] = dist[p]+1
        Q.append(q)
        if len(dist) == n+k: break
print(sum(dist.values()))