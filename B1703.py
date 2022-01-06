while True :
    a = list(map(int, input().split()))
    if (a[0] == 0) :
        break
    ans = 1
    for i in range(a[0]) :
        ans *= a[i * 2 + 1]
        ans -= a[i * 2 + 2]
    print(ans)

while True:
    n=list(map(int,input().split()))
    if n[0]==0:break
    s=1
    for i in range(1,n[0]*2,2):
        s*=n[i]
        s-=n[i+1]
    print(s)