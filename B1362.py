num = 0
while (True) :
    num += 1
    o, w = map(int, input().split())
    if o == 0 and w == 0 :
        break
    d = False
    while (True) :
        s = input().split()
        n = int(s[1])
        if '#' in s :            
            break
        elif 'E' in s :
            w -= n
        else :
            w += n
        if w <= 0 :
            d = True
    if d :
        print(num, "RIP")
    elif o / 2 < w and w < o * 2 :
        print(num, ":-)")
    else :
        print(num, ":-(")


T=1
while T:
    o,w=map(int,input().split())
    if o+w==0:break
    W,l=w,1
    A,B=input().split()
    while 1:
        if A=='F':W+=int(B)
        else:W-=int(B)
        if W<=0:l=0
        A,B=input().split()
        if A+B=='#0':break
    if l:print(T,':-)'if o*.5<W<2*o else':-(')
    else:print(T,'RIP')
    T+=1