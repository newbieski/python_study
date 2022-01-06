a, b = map(int, input().split())
c, d = max(a, b), min(a, b)
ans = 0
for i in range(150) :
    if i * i > c + d :
        break
    a = b = int(i * i / 2)
    if i % 2 == 1 :
        a += 1
    if c >= a and d >= b :
        ans = i
if ans == 0 : 
    print("Impossible")
else :
     print(ans)


n,m=sorted(map(int,input().split()))
k=int((2*n+(n<m))**.5)
print([k,'Impossible'][not k])


b,w=map(int,input().split())
b,w=min(b,w),max(b,w)
I=0
while b>=I*I//2 and w>=I*I-I*I//2:I+=1
I-=1
if I==0:print('Impossible')
else:print(I)