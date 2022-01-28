"""
import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
sys.setrecursionlimit(n + 10)
adj = [[] for _ in range(n + 1)]
incnt = [0] * (n + 1)
dcnt, gcnt = 0, 0
edge = []
for _ in range(n - 1) :
    a, b = map(int, input().split())
    incnt[a] += 1
    incnt[b] += 1
    edge.append((a, b))    

def nc3(n) :
    return n * (n - 1) * (n - 2) // 6

for a, b in edge :
    dcnt += (incnt[a] - 1) * (incnt[b] - 1)

for i in range(1, n + 1) :
    if incnt[i] >= 3 :
        gcnt += nc3(incnt[i])

if dcnt > gcnt * 3 : print("D")
elif dcnt < gcnt * 3 : print("G")
else : print("DUDUDUNGA")
"""

import sys
input = sys.stdin.readline
n = int(input())
sys.setrecursionlimit(n + 10)
adj = [[] for _ in range(n + 1)]
incnt = [0] * (n + 1)
dcnt, gcnt = 0, 0
for _ in range(n - 1) :
    a, b = map(int, input().split())
    incnt[a] += 1
    incnt[b] += 1
    adj[a].append(b)
    adj[b].append(a)

def dfs(prev, cur) :
    c3, c2, c1 = 0, 0, 0
    for nxt in adj[cur] :
        if nxt == prev : continue
        n3, n2, n1 = dfs(cur, nxt)
        c1 += 1
        c2 += n1
        c3 += n2
        global dcnt
        dcnt += n3
    return c3, c2, c1        

def nc3(n) :
    return n * (n - 1) * (n - 2) // 6

n3, n2, n1 = dfs(0, 1)
dcnt += n3

for i in range(1, n + 1) :
    if incnt[i] >= 3 :
        gcnt += nc3(incnt[i])

if dcnt > gcnt * 3 : print("D")
elif dcnt < gcnt * 3 : print("G")
else : print("DUDUDUNGA")
