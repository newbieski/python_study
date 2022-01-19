import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
mrx = [[False] * (n + 1) for _ in range(n + 1)]
cnt = [0] * (n + 1)
e = []
ans = 12000
for _ in range(m) :
    u, v = map(int, input().split())
    mrx[u][v] = mrx[v][u] = True
    e.append((u, v))
    cnt[u] += 1
    cnt[v] += 1
for i in e :
    for j in range(1, n + 1) :
        if j in i : continue
        u, v = i
        if mrx[j][u] and mrx[j][v] : ans = min(ans, cnt[u] + cnt[v] + cnt[j] - 6)
if ans == 12000 : ans = -1
print(ans)


import sys

n, m = map(int, input().split())
relations = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

friends = [set() for _ in range(n)]
for relation in relations:
    friends[relation[0]-1].add(relation[1])
    friends[relation[1]-1].add(relation[0])

num_friends = m
flag = False
for a in range(n):
    for b in friends[a]:
        if b > a:
            for c in friends[b-1]:
                if c in friends[a] and c > b:
                    num_friends = min(num_friends, len(friends[a]) + len(friends[b-1]) + len(friends[c-1]) - 6)
if num_friends < m:                
    print(num_friends)
else:
    print(-1)

