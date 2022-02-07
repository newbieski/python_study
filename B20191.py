import sys
sys.stdin = open("input.in", "r")

def lowerbound(a, k) :
    l, r = 0, len(a) - 1
    while (l < r) :
        mid = (l + r) // 2
        if a[mid] >= k :
            r = mid
        else :
            l = mid + 1
    if a[r] < k : r = -1
    return r

input = sys.stdin.readline
s = input().strip()
t = input().strip()

l = [[] for _ in range(128)]
for i in range(len(t)) :
    l[ord(t[i])].append(i)

def sol() :
    res = 1
    cur = 0
    for c in s :
        if cur == len(t) :
            res += 1
            cur = 0

        src = l[ord(c)]
        if len(src) == 0 : return -1
        tmp = lowerbound(src, cur)        
        if tmp != -1 : tmp = src[tmp]        
        if cur <= tmp :
            cur = tmp + 1
        else :
            res += 1
            tmp = lowerbound(src, 0)            
            tmp = src[tmp]
            cur = tmp + 1
    return res

print(sol())

