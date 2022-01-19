import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
m = list(map(int, input().split()))
x = []
min = 50000
minv = [15, 15, 15]
def calc(k) :
    global min, minv
    tmp = []
    for i in range(n) :
        if k & (1<<i) :
            tmp.append(i)
    arr = [0] * 5
    for i in tmp :
        for j in range(5) :
            arr[j] += x[i][j]
    if (arr[4] > min) : return
    for i in range(4) :
        if arr[i] < m[i] : return
    
    if (arr[4] < min) :
        min = arr[4]
        minv = list(tmp)
    elif arr[4] == min and tmp < minv :
        minv = list(tmp)

for _ in range(n) :
    x.append(list(map(int, input().split())))

for i in range(2**n) :
    calc(i)
if min == 50000 : print(-1)
else : 
    print(min)
    print(" ".join([str(i+1) for i in minv]))


from itertools import combinations
MIS = lambda: map(int,input().split())

n = int(input())
mp, mf, ms, mv = MIS()
ing = [tuple(MIS()) for i in range(n)]
cand = []
for sz in range(1, n+1):
    for C in combinations(range(1,n+1), sz):
        money = 0
        P, F, S, V = 0, 0, 0, 0
        for i in C:
            p, f, s, v, cost = ing[i-1]
            P+= p; F+= f; S+= s; V+= v
            money+= cost
        if P>=mp and F>=mf and S>=ms and V>=mv:
            cand.append((money,)+C)
if cand: print(*min(cand))
else: print(-1)
