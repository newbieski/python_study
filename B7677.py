import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
MOD = 10000

def mat_mul(a, b) :
    res = [[0] * 2 for _ in range(2)]
    for i in range(2) :
        for j in range(2) :
            for k in range(2) :
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= MOD
    return res

def mat_pow(a, x) :
    if x == 1 : return list(a)
    res = mat_pow(a, x //2)
    res = mat_mul(res, res)
    if x % 2 == 1 : res = mat_mul(res, a)
    return res

b = [[1, 1], [1, 0]]
while True :
    n = int(input())    
    if n == -1 : break
    ans = mat_pow(b, n + 1)
    print(ans[1][1])
