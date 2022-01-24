import sys
sys.stdin = open("input.in", "r")
che = [0] * 1001
primes = []
MOD = 1000000009

for i in range(2, 1001) :
    if che[i] :        
        continue
    primes.append(i)
    for j in range(i, 1001, i) :
        che[j] = i

psz = len(primes)

fd = []
fd.append([])
fd.append([0] * psz)
for i in range(2, 1001) :
    cur = list(fd[i - 1])
    j = i
    while j != 1 :
        k = che[j]
        cur[primes.index(k)] += 1
        j //= k
    fd.append(cur)

n, k = map(int, input().split())
cur = []
for kk in range(k + 1) :
    cur.append([0] * psz)
for nn in range(2, n + 1) :
    prev = cur
    cur = [[]]
    cur.append(list(fd[nn]))
    for kk in range(2, k + 1) :
        cur.append([a + b for a, b in zip(cur[kk - 1], prev[kk])])

ans = 1
for i in cur[k] :
    ans *= (i + 1)
print(ans % MOD)