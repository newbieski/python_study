import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
m = int(input())
sys.setrecursionlimit(n + 10)
f = []
adj = [[] for _ in range(n + 1)]
pr = [i for i in range(n + 1)]

def find(a) :
    global pr
    if a == pr[a] : return a
    pr[a] = find(pr[a])
    return pr[a]

def union(a, b) :
    global pr
    a, b = find(a), find(b)
    pr[a] = b

for _ in range(m) :
    a, p, q = input().split()
    p, q = int(p), int(q)
    if a == 'E' :
        adj[p].append(q)
        adj[q].append(p)
    else :
        f.append((p, q))

for i in range(1, n + 1) :
    for j in adj[i] :
        for k in adj[j] :
            f.append((i, k))

for p, q in f :
    union(p, q)

ans = set()
for i in range(1, n + 1) :
    ans.add(find(i))
print(len(ans))