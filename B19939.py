n, k = map(int, input().split())
p = n - (k*(k-1)//2)
a = p//k
b = a + k - 1
if p % k : b += 1
if a > 0 : print(b - a)
else : print(-1)


n,k=map(int,input().split())
n-=(k+1)*k//2
if n<0:e=-1
elif n%k:e=k
else:e=k-1
print(e)