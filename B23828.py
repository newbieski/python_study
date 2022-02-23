import sys
sys.stdin = open("input.in", "r")
MOD = 10**9+7
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0 for _ in range(100001)]
s = set()
for i in a :
    cnt[i] += 1
    s.add(i)
dp = [0 for _ in range(m + 1)]
dp[0] = 1
for i in s :
    for j in range(m - 1, -1, -1) :
        dp[j + 1] += dp[j] * i * cnt[i]
        dp[j + 1] %= MOD
print(dp[m])