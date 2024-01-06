import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
def cnt(a, b) :
    sum = 0
    for p, q in zip(a, b) :
        sum += abs(p-q)
    return sum > 2000
n,m=map(int, input().split())
lal = list(map(int, input().split()))
anti = 0
for _ in range(n - 1) :
    x = list(map(int, input().split()))
    anti += cnt(lal, x)
if anti * 2 >= n
    print("YES")
else :
    print("NO")