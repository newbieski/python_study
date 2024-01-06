m=2**64
n=int(input())
L=list(map(int,input().split()))
R=list(map(int,input().split()))

def f(x) :
    value = x
    for l,r in zip(L,R) :
        if l <= x and x <= r :
            value ^= (((x|l)+(x&r)*(l^r)) % m)
    return value >= 0x0123456789ABCDEF

def sol() :
    lf,rt=0,10**18+1
    while lf + 1 < rt :
        mid = (lf + rt) // 2
        if f(mid) :
            rt = mid
        else :
            lf = mid
    return lf
print(sol())
