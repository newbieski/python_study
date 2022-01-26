n,a,b,c,d=map(int, input().split())
print(min((n-1)//a*b+b,(n-1)//c*d+d))

n,a,b,c,d=map(int,input().split())
print(-max((n//-a)*b,(n//-c)*d))