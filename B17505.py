n,k=map(int,input().split())
ans, l, h =[], 1, n
for i in range(n) :
    if k >= n - i - 1 :
        ans.append(h)
        h -= 1
        k -= (n - i - 1)
    else :
        ans.append(l)
        l += 1
print(*ans)