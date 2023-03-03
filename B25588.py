import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n,k=map(int,input().split())
dp = [n for _ in range(n + 1)]
l = [i for i in range(n + 1)]
ai = [20]
ai.extend(list(map(int, input().split())))

dp[0] = 0
for i in range(1, n + 1) :
    if abs(ai[i] - ai[i - 1]) == 1 :
        l[i] = l[i - 1]
    for j in range(1, 4) :
        if i - j < 0 :
            break
        dp[i] = min(dp[i], 1 + dp[i - j])
    if i - l[i] + 1 >= k :
        dp[i] = min(dp[i], 1 + dp[i - k])
    
print(dp[n])