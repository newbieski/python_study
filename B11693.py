MOD = 1000000007
che = [False] * 31623
p = []

for i in range(2, 31623) :
    if not che[i] :
        for j in range(i * i, 31623, i) :
            che[j] = True
for i in range(2, 31623) :
    if not che[i] : p.append(i)

def sums(a, r) :
    return (pow(a, r + 1, MOD) + MOD - 1) * pow((a - 1), -1, MOD) % MOD

n, m = map(int, input().split())
ans = 1
for i in p :
    if n % i : continue
    r = 0
    while n % i == 0 :
        r += 1
        n //= i
    ans *= sums(i, r * m)
    ans %= MOD
if n != 1 :
    ans *= sums(n, m)
    ans %= MOD
print(ans)
