import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x = min(n, m)
a = sorted(map(int, input().split()), reverse = True)
b = sorted(map(int, input().split()))

ans = 0
for i,j in zip(a, b) :
    if i < j : break
    ans += i - j
print(ans)