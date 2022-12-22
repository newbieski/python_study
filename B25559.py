n=int(input())
if n == 1 :
    print(1)
elif n * (n + 1) // 2 % n == 0 :
    print(-1)
else :
    ans=[str(n)]
    a,b=n-1,2
    sum = n
    for _ in range(n//2) :
        ans.append(str(a))
        ans.append(str(b))        
        a -= 2
        b += 2
    print(" ".join(ans[:-1]))