def sol() :
    x,y,p1,p2 = map(int, input().split())
    a = []
    b = p1
    for i in range(p1 * p2 + 1) :
        a.append(b)
        b += x
    b = p2
    for i in range(p1 * p2 + 1) :
        if b in a : return b
        b += y
    return -1

print(sol())


x,y,p1,p2=map(int,input().split())
set1=set(range(p1,10000,x))
set2=set(range(p2,10000,y))
try:
    print(min(set1&set2))
except:
    print(-1)