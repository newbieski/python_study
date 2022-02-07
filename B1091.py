import sys
sys.stdin = open("input.in", "r")
n = int(input())
tobe = list(map(int, input().split()))
trans = list(map(int, input().split()))
cur = [i for i in range(n)]

def isfinish() :
    for i in range(n) :
        if tobe[cur[i]] != i % 3 : return False
    return True

def isstart() :
    for i in range(n) :
        if cur[i] != i : return False
    return True

def dotrans() :
    nxt = [0] * n
    for i in range(n) :
        nxt[trans[i]] = cur[i]
    return nxt

ans, fin = 0, False
while True :
    if isfinish() :
        fin = True
        break
    cur = dotrans()
    ans += 1
    if isstart() : break
if fin : print(ans)
else : print(-1)