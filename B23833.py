import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10000)
tr = [1 for _ in range(2**18)]
n, q = map(int, input().split())
flo = list(map(int, input().split()))

def seginit(node, s, e) :
    global tr
    if s == e :
        return 1
    else :
        mid = (s + e) // 2
        tr[node] = seginit(node * 2, s, mid) + seginit(node * 2 + 1, mid + 1, e)
        if flo[mid] == flo[mid + 1] :
            tr[node] -= 1        
        return tr[node]

def segsum(node, s, e, l, r) :
    global tr
    if r < s or e < l :
        return 0
    if l <= s and e <= r :
        #print("segsum", node, s, e, tr[node])
        return tr[node]
    else :
        mid = (s + e) // 2
        res = segsum(node * 2, s, mid, l, r) + segsum(node * 2 + 1, mid + 1, e, l, r)
        if l <= mid and mid + 1 <= r and flo[mid] == flo[mid + 1] :
            res -= 1
        #print("segsum", node, s, e, res)
        return res
    
def segupdate(node, s, e, l) :
    global tr
    if l < s or e < l : return tr[node]
    if s == e :
        #print("segupdate", node, s, e, tr[node])
        return 1
    else :
        mid = (s + e) // 2
        tr[node] = segupdate(node * 2, s, mid, l) + segupdate(node * 2 + 1, mid + 1, e, l)
        if flo[mid] == flo[mid + 1] :
            tr[node] -= 1
        #print("segupdate", node, s, e, tr[node])
        return tr[node]


flo.insert(0, 0)
seginit(1, 1, n)
for _ in range(q) :
    ti, a, b = map(int, input().split())
    if ti == 1 :
        #print(flo)
        print(segsum(1, 1, n, a, b))
    else :
        flo[a] = b
        segupdate(1, 1, n, a)