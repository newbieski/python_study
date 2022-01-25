import sys
input = sys.stdin.readline

n, q = map(int, input().split())
p = [i for i in range(n + 1)]
xs = []

def find(a) :
    if a == p[a] : return a
    p[a] = find(p[a])
    return p[a]

def union(a, b) :
    a, b = find(a), find(b)
    p[a] = b

for i in range(1, n + 1) :
    x1, x2, y = map(int, input().split())
    xs.append((x1, x2, i))
xs.sort()

x, prev = -1, 0
for x1, x2, i in xs :
    if x1 <= x :
        #union(prev, i)
        union(i, prev)
        if x < x2 : x, prev = x2, i
    else :
        x, prev = x2, i

while q > 0 :
    q -= 1
    a, b = map(int, input().split())
    if find(a) == find(b) : print(1)
    else : print(0)