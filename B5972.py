import sys
import queue
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
dist = [50000100] * (n + 1)
while m > 0:
    m -= 1
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

pq = queue.PriorityQueue()
dist[1] = 0
pq.put((0, 1))
while not pq.empty() :
    d, a = pq.get()
    if dist[a] < d : continue
    for i in adj[a] :
        b, c = i
        nxtc = dist[a] + c
        if nxtc < dist[b] :
            dist[b] = nxtc
            pq.put((nxtc, b))
print(dist[n])

import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())
N, M = MIIS()
roads = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = MIIS()
    roads[a].append((b, c))
    roads[b].append((a, c))
heap = [(0, 1)]
visited = [False] * (N + 1)
while heap:
    d, cow = heapq.heappop(heap)
    if cow == N:
        print(d)
        break
    if visited[cow]:
        continue
    visited[cow] = True
    for b, c in roads[cow]:
        if not visited[b]:
            heapq.heappush(heap, (d + c, b))
