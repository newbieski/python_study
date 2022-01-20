import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
cnt = dict()
p = []

def gcd(a, b) :
    if b == 0 : return a
    return gcd(b, a % b)

n = int(input())
for _ in range(n) :
    a, b, c = map(int, input().split())
    if a == 0 : b = 1
    elif b == 0 : a = 1
    else :
        s = 1
        if a < 0 : 
            a = -a
            s *= -1
        if b < 0 : 
            b = -b
            s *= -1
        g = gcd(a, b)
        a /= g
        b /= g
        a *= s
    val = (a, b)
    cnt.setdefault(val, 0)
    if cnt[val] == 0 :
        p.append(val)
    cnt[val] += 1

sum, comb, ans, mod = 0, 0, 0, 1000000007

for i in p :
    ans += cnt[i] * comb
    comb += sum * cnt[i]
    sum += cnt[i]
    ans %= mod
    comb %= mod
    sum %= mod
print(ans)


import math
from collections import defaultdict as d
N=int(input())
q,r,l=0,N,d(int)
while r:a,b,c=map(int,input().split());g=math.gcd(a,b);l[a/g,b/g]+=1;r-=1;q+=r*r-r
for i in l:j=l[i];q-=(3*N-2*j-2)*(j*j-j)//3
print(q//2%(10**9+7))


import math
import sys
input = sys.stdin.readline
mod = 1000000007

N = int(input())
line = []
for _ in range(N):
	a, b, c = map(int, input().split())
	d = math.gcd(a, b)
	a = a // d
	b = b // d
	line.append((a, b))
line = sorted(line, key=lambda x:(x[0], x[1]))
line.append((mod, mod))

multiple = []
ans = N * (N-1) * (N-2) // 6

count = 1
for i in range(0, N):
    if line[i] == line[i+1]:
        count += 1
    else:
        multiple.append(count)
        count = 1

for j in multiple:
    miss = (N-j) * j * (j-1) // 2
    ans -= miss
    if j > 2:
        miss = j * (j-1) * (j-2) // 6
        ans -= miss

print(ans % mod)