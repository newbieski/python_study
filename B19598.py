import sys
import heapq
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n) :
    a.append(tuple(map(int, input().split())))
a.sort()
pq = [0]
for s, e in a :
    if pq[0] <= s :
        heapq.heappop(pq)
    heapq.heappush(pq, e)
print(len(pq))