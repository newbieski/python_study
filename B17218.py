import sys
s1 = input()
s2 = input()
n1, n2 = len(s1), len(s2)
s1 = "_" + s1
s2 = "_" + s2
ans, p1, p2 = 0, 0, 0
dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

for i in range(1, n1 + 1) :
    for j in range(1, n2 + 1) :
        if s1[i] == s2[j] :
            dp[i][j] = dp[i - 1][j - 1] + 1
        else :
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if ans < dp[i][j] :
            ans, p1, p2 = dp[i][j], i, j
ans_str = ""
while 0 < p1 and 0 < p2 :
    if s1[p1] == s2[p2] : 
        ans_str = s1[p1] + ans_str
        p1 -= 1
        p2 -= 1
    elif dp[p1 - 1][p2] > dp[p1][p2 - 1] :
        p1 -= 1
    else :
        p2 -= 1
print(ans_str)