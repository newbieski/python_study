import sys
sys.stdin = open("input.in", "r")
MOD = 1000
def mul(a, b) :
    res = [[0] * 2 for _ in range(2)]
    for i in range(2) :
        for j in range(2) :
            for k in range(2) :
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= MOD
    return res

def mul_pow(a, x) :
    if x == 1 : return a
    tmp = mul_pow(a, x // 2)
    tmp = mul(tmp, tmp)
    if x % 2 == 1 : tmp = mul(tmp, a)
    return tmp
tt = int(input())
a1, a2 = 6, 28
for tc in range(1, tt + 1) :
    n = int(input())
    p = ((6, -4), (1, 0))
    p = mul_pow(p, n - 1)
    an = p[1][0] * a2 + p[1][1] * a1
    print(f'Case #{tc}: ' + '%03i' % ((MOD + an - 1) % MOD))
    

    
