import sys

sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
thr = []
for _ in range(n) :
    thr.append(tuple(map(int, input().split())))
thr.sort()

def check(k) :
    prev = thr[0][0] - k
    for x, l in thr :
        cur = prev + k
        if cur < x : cur = x
        elif x + l < cur : return False
        prev = cur
    return True

l, r, ans = 1, 2000000001, 0
while l <= r :
    mid = (l + r) // 2
    if check(mid) :
        if ans < mid : ans = mid
        l = mid + 1
    else : r = mid - 1
print(ans)