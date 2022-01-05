import sys
sys.stdin = open("input.in", "r")

def conv() :
    l1 = list(map(int, input().split()))
    l2 = list(set(l1))
    l2.sort()
    res = 0
    for i in l1 :
        res *= 10
        res += l2.index(i) + 1
    return res

m, n = map(int, input().split())
l = []
ans = 0
for i in range(m) :
    l.append(conv())
for i in l :
    ans +=  l.count(i) - 1
print(ans//2)


def compress(L):
    d = {}
    for i, x in enumerate(sorted(L)): d[x] = i
    return tuple(map(d.__getitem__, L))

from collections import Counter
n, m = map(int,input().split())
C = Counter(map(compress, [list(map(int,input().split())) for i in range(n)]))
print(sum(v*(v-1)//2 for v in C.values()))