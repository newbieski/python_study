n = int(input())
p = [0 for _ in range(n + 1)]

for i in range(2, n + 1) :
    if p[i] == 0 :
        for j in range(i, n + 1, i) :
            p[j] = i
def f(k) :
    res = set()
    while p[k] :
        res.add(p[k])
        k = k // p[k]
    return list(res)

def in_ex(k) :
    q = f(k)
    l = len(q)
    sum = n - k
    for i in range(1, 1<<l) :
        cnt, a = 0, 1
        for j in range(l) :
            if i & (1<<j) :
                cnt += 1
                a *= q[j]
        tmp = n // a - k // a
        if cnt & 1 : sum -= tmp
        else : sum += tmp
    return sum
ans = 0
for i in range(1, n + 1) :
    ans += in_ex(i)
print(ans)
                