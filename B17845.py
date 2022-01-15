import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [-1] * (n + 1)
dp[0] = 0
while k > 0 :
    k -= 1
    a, b = map(int, input().split())
    for i in range(n - b, -1, -1) :
        if dp[i] == -1 : continue
        dp[i + b] = max(dp[i + b], dp[i] + a)
print(max(dp))