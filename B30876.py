a,b=0,1001
for _ in range(int(input())) :
    x,y=map(int,input().split())
    if y < b : a,b=x,y
print(a,b)