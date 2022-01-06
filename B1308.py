def leaf_year(y1) :
    if y1 % 400 == 0 : return 29
    if y1 % 100 == 0 : return 28
    if y1 % 4 == 0 : return 29
    return 28

ld = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y,m,d = map(int, input().split())
ey,em,ed = map(int, input().split())
ans = 0
sy,sm,sd = y,m,d
ld[2] = leaf_year(y)

while True :
    if sy + 1000 == y and sm == m and sd == d :
        ans = -1
        break
    if y == ey and m == em and d == ed :
        break
    ans += 1
    d += 1
    if d == ld[m] + 1 :
        d = 1
        m += 1
    if m == 13 :
        m = 1
        y += 1
        ld[2] = leaf_year(y)
if ans == -1 : print("gg")
else : print(f'D-{ans}')



def dday(x, y, z):
    s=z-1
    for i in range(1, x):
        s+=365+int((i%4==0 and i%100>0) or i%400==0)
    A=[31,28+int((x%4==0 and x%100>0) or x%400==0),31,30,31,30,31,31,30,31,30]
    for i in range(y-1):
        s+=A[i]
    return s
a, b, c=map(int, input().split())
d, e, f=map(int, input().split())
if 10000*a+100*b+c+10000000<=10000*d+100*e+f:
    print('gg')
else:
    print('D-', end='')
    print(dday(d, e, f)-dday(a, b, c))