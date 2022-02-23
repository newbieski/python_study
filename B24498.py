import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = max(a)
for i in range(1, n - 1) :
    ans = max(ans, min(a[i - 1], a[i + 1]) + a[i])
print(ans)