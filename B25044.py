n,k=map(int, input().split())
ans=[]
stop = [15*60, 18*60, 21*60]
actm, cnt, w = 0, 0, 0
d = 24*60
for cur in range(d*(n + 1)) :
    if w > 0 :
        w -= 1
        continue
    if actm in stop :
        cnt += 1
        if cur >= n * d :
            ans.append((cur%d//60, cur%d%60))
        if cnt % 3 == 0  :
            w = k
    actm += 1
    actm %= d
print(len(ans))
for i in ans :
    print('%02d:%02d' % i)