n=int(input())
print(n*(n-1)//2)
a,b = 1,1
ans=[]
for _ in range(n) :
    #ans.append(str(a))
    ans.append(str(a))
    a += b
    b *= 2
print(" ".join(ans))
print(n-1)
ans=[str(i) for i in range(1, n + 1)]
print(" ".join(ans))