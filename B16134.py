n, r = map(int, input().split())
MOD =  1000000007
res = 1
a, b = n, 1
for _ in range(r) :
    res *= a
    res *= pow(b, MOD - 2, MOD)
    a -= 1
    b += 1
    res %= MOD
print(res)