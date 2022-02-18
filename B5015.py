import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
tmp = input().strip()
p = ""
for i in range(len(tmp)) :
    if i > 0 and tmp[i] == '*'and tmp[i] == tmp[i - 1] :
        continue
    else : p += tmp[i]

n = int(input())
def sol(f) :
    dp = []
    if p[0] == '*' :
        dp.append([1 for _ in range(len(f))])
    else :
        dp.append([0 for _ in range(len(f))])
        if p[0] == f[0] :
            dp[0][0] = 1

    for i in range(1, len(p)) :
        tmp = []
        for j in range(len(f)) :
            if p[i] == '*' :
                res = 0
                for k in range(j + 1) :
                    res |= dp[i - 1][k]
            elif p[i] == f[j] :
                if j > 0 : res = dp[i - 1][j - 1]
                elif i - 1 == 0 and p[i - 1] == '*' : res = 1
                else : res = 0
            else :
                res = 0
            tmp.append(res)
        dp.append(tmp)
    return dp[len(p) - 1][len(f) - 1]
    
for _ in range(n) :
    f = input().strip()
    if sol(f) : print(f)



def reg(x, p):
    xl, pl = len(x), len(p)
    dp = [[0 for _ in range(xl+1)] for _ in range(pl+1)]
    dp[0][0] = 1
    for i in range(1, pl+1):
        if p[i-1] == '*':
            ck = 0
            for j in range(xl+1):
                if dp[i-1][j] : ck = 1
                dp[i][j] = ck
        else :
            for j in range(1, xl+1):      
                if dp[i-1][j-1] and p[i-1] == x[j-1] : dp[i][j] = 1
    
    if dp[pl][xl] : print(x)

pattern = input()
for _ in range(int(input())): reg(input(), pattern)