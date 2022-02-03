n, m = map(int, input().split())
p = list(map(int, input().split()))
ans = 0
for i in range(1, 1<<n) :
    cnt, tmp = 0, 1
    for j in range(n) :
        if tmp > m : break
        if i & (1<<j) :
            cnt += 1
            tmp *= p[j]
    if tmp > m : continue
    if cnt & 1 : ans += m // tmp
    else : ans -= m // tmp
print(ans)