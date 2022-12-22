import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n=int(input())
s=list(map(int, input().split()))
e=s[2:]
def mht(a,b) :
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
ans, mn = 0, 10**20
for nv in range(1, n + 1) :
    n = int(input())
    prev,sum = s,0
    for _ in range(n) :
        cur = list(map(int, input().split()))
        sum += mht(prev, cur)
        prev = cur
    sum += mht(prev, e)    
    if sum < mn :
        mn, ans = sum, nv
print(ans)

