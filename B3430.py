import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
MAX = 10**7
SZ = (1<<20)

tr = []

def init() :
    global tr
    tr = [MAX for _ in range(SZ * 2)]

def idx_min(l, r) :
    res = MAX
    l += SZ - 1
    r += SZ - 1
    while l <= r :
        if l & 1 : res = min(res, tr[l])
        l = (l + 1) // 2
        if (r & 1) == 0 : res = min(res, tr[r])
        r = (r - 1) // 2
    return res

def idx_update(l, v) :
    global tr
    l += SZ - 1
    tr[l] = v
    l //= 2
    while l >= 1 :
        tr[l] = min(tr[l * 2], tr[l * 2 + 1])
        l //= 2

tt = int(input())
while tt > 0 :
    tt -= 1
    init()
    n, m = map(int, input().split())
    rday = []
    lpos = [1 for _ in range(n + 1)]
    ans = [0 for _ in range(m + 1)]
    info = [0]
    info.extend(list(map(int, input().split())))    
    
    suc = True
    for i in range(m + 1) :
        cur = info[i]
        if cur == 0 :
            rday.append(i)
            idx_update(i, i)
        else :
            p = idx_min(lpos[cur], i)
            if p == MAX :
                suc = False
                break
            else :
                ans[p] = cur
                lpos[cur] = i
                idx_update(p, MAX)
    
    if suc :
        print("YES")        
        print(*[ans[i] for i in rday][1:])
    else :
        print("NO")
