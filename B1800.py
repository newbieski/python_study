import sys
import queue
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

n, p, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(p) :
    a, b, d = map(int, input().split())
    adj[a].append((b, d))
    adj[b].append((a, d))

def bfs(x) :
    pq = queue.PriorityQueue()
    cnt = [2000 for _ in range(n + 1)]
    cnt[1] = 0
    pq.put((0, 1))
    while not pq.empty() :
        curcnt, cur = pq.get()
        if cnt[cur] < curcnt : continue
        for b, d in adj[cur] :
            nxtcnt = curcnt
            if d > x : nxtcnt += 1
            if nxtcnt < cnt[b] :
                cnt[b] = nxtcnt
                pq.put((nxtcnt, b))
    return cnt[n] <= k

l, r, ans = 0, 1000000, 2000000
while (l <= r) :
    mid = (l + r) // 2
    if bfs(mid) :
        ans = min(ans, mid)
        r = mid - 1
    else : l = mid + 1
if ans == 2000000 : ans = -1
print(ans)