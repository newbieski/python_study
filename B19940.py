import sys
input = sys.stdin.readline

tt = int(input())

def arr_comp(a, b) :
    if a[5] < b[5] : return True
    if a[5] > b[5] : return False
    for i in range(5) :
        if a[i] < b[i] : return True
    return False

def find(a) :
    p = a // 6
    r = a % 6
    t1 = [p, r, 0, 0, 0, p + r]
    t2 = [p + 1, 0, 6 - r, 0, 0, p + 1 + 6 - r]
    if arr_comp(t1, t2) : return t1
    return t2

def sol(a) :
    p = a // 10
    r = a % 10
    t1 = find(p)
    t1[3] += r
    t1[5] += r
    t2 = find(p + 1)
    t2[4] += 10 - r
    t2[5] += 10 - r
    if arr_comp(t1, t2) : return t1
    return t2

while tt > 0 :
    tt -= 1
    ans = sol(int(input()))
    print(" ".join([str(i) for i in ans[:5]]))