a=[]
for _ in range(int(input())) :
    s,t=input().split()
    a.append(list(t.upper())[list(s.upper()).index('X')])
print(*a,sep='')
