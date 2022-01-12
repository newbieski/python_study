import sys
input = sys.stdin.readline
mod = 1000000007

def mypow(e, x) :
    if x == 0 : return 1
    tmp = mypow(e, x // 2)
    tmp *= tmp
    if x % 2 == 1 : tmp *= e
    return tmp % mod

m = int(input())
ans = 0
while m > 0 :
    m -= 1
    n, s = map(int, input().split())
    ans += s * mypow(n, mod - 2)
    ans %= mod
print(ans)

M=10**9+7;print(sum(int(i.split()[1])*pow(int(i.split()[0]),-1,M)for i in[*open(0)][1:])%M)