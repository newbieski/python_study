import sys
import collections
sys.stdin = open("input.in", "r")
iii = []
for _ in range(3) :
    try :
        k, s = input().split()
        iii.append(s)
    except :
        iii.append("")
iii = tuple(iii)

def check(s) :
    a = ["A", "B", "C"]
    for key, str in zip(a, s) :
        if str.count(key) != len(str) : return False
    return True

def gen(s, e, strs) :
    res = list(strs)
    if len(res[s]) != 0 : 
        res[e] = res[e] + res[s][-1]
        res[s] = res[s][:-1]
    return tuple(res)

def sol() :
    vt = collections.defaultdict(int)
    vt[iii] = 1
    q = collections.deque()
    q.append(iii)
    while len(q) > 0 :
        cur = q.popleft()
        if check(cur) : return vt[cur] - 1
        nxts = []
        
        for i in range(3) :
            for j in range(3) :
                if i != j : nxts.append(gen(i, j, cur))
        for nxt in nxts :
            if vt[nxt] == 0 :
                vt[nxt] = vt[cur] + 1
                q.append(nxt)

print(sol())