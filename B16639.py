import sys
sys.stdin = open("input.in", "r")
n = int(input())
exp = input().strip()
cache = []
for _ in range(n + 1) :
    cache.append([(False, 0, 0) for _ in range(n + 1)])

def dp(l, r) :
    vt, b, c = cache[l][r]
    if vt : return b, c
    if l == r + 1 :
        b = c = int(exp[l])
        c = b
        cache[l][r] = (True, b, c)
        return b, c
    b = c = eval(exp[l:r])
    for i in range(l + 1, r, 2) :
        b1, c1 = dp(l, i)
        b2, c2 = dp(i + 1, r)
        for x in b1, c1 :
            for y in b2, c2 :                
                s = eval(str(x) + exp[i] + str(y))
                b = min(b, s)
                c = max(c, s)
    
    cache[l][r] = (True, b, c)
    return b, c

print(dp(0, n)[1])