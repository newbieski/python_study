import sys
sys.stdin = open("input.in", "r")

input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] * n
for i in range(n) :
    a[i] = int(input())
a.sort()

p = {}
j = 0
for i in a :
    if p.get(i, -1) == -1 :
        p[i] = j
    j += 1

while m > 0 :
    m -= 1
    print(p.get(int(input()), -1))



n,m,*l = map(int, open(0).read().split())
d={}
for i,v in enumerate(sorted(l[:n])):
    d[v]=d.get(v,i)
print(*[d.get(i, -1) for i in l[n:]],sep='\n')

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
indexs = {}
for idx,a in enumerate(arr):
    if indexs.get(a) is None:
        indexs[a] = idx

for _ in range(M):
    d = int(input())
    try:
        print(indexs[d])
    except KeyError:
        print(-1)