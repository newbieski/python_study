import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sys.setrecursionlimit(n + 10)
p = [*range(n + 1)]

def find(a) :
    global p
    if a == p[a] : return a
    p[a] = find(p[a])
    return p[a]

def union(a, b) :
    global p
    a, b = find(a), find(b)
    if a == b : return False
    p[a] = b
    return True

def sol() :
    for i in range(m) :
        a, b = map(int, input().split())
        if not union(a, b) : return i + 1
    return 0

print(sol())