while (True) :
    a, b, c, d = map(int, input().split())
    if (a + b + c + d == 0) :
        break
    e = min(c * 100 // a, d * 100 // b)
    f = min(c * 100 // b, d * 100 // a)
    ans = max(e, f)
    if (ans > 100) :
        ans = 100
    print(f'{ans}%')


while any(l:=[*map(int,input().split())]):a,b,c,d=l;c*=100;d*=100;print(f'{max(min(c//a,d//b,100),min(c//b,d//a,100))}%')

s=input()
while '0 0' not in s:
 a,b,c,d=map(int,s.split())
 r=int(min(min(c,d)/min(a,b),max(c,d)/max(a,b))*100)
 print(str((r,100)[r>100])+'%' )
 s=input()