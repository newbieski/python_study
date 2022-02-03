import sys
sys.stdin = open("input.in", "r")
MAX = 1000000
input = sys.stdin.readline
n = int(input())
sys.setrecursionlimit(MAX + 10)
p = list(range(MAX + 1))
sz = [1] * (MAX + 1)

def find(a) :
    global p
    if a == p[a] : return a
    p[a] = find(p[a])
    return p[a]

def union(a, b) :
    a, b = find(a), find(b)
    global p, sz
    if a != b :
        p[a] = b
        sz[b] += sz[a]

for _ in range(n) :
    s = input().split()
    if s[0] == 'I' : union(int(s[1]), int(s[2]))
    elif s[0] == 'Q' : print(sz[find(int(s[1]))])