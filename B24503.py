import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
k, q = map(int, input().split())
ai = list(map(int, input().split()))
def gcd(a, b) :
    if b == 0 : return a
    return gcd(b, a % b)

def facto(a) :
    i = 2
    res = []
    while i * i <= a :
        if a % i == 0 :
            res.append(i)
            while a % i == 0 :
                a //= i
        i += 1
    if a != 1 : res.append(a)
    return res

def f(a, b) :
    res = 0
    while b > 0 :
        res += a
        i = res
        while i % a == 0 :
            b -= 1
            i //= a
    return res

p = facto(k)

ans = []
for i in ai :
    g = gcd(k, i)
    res = 0
    tmp = k // g
    for j in p :
        cnt = 0
        while tmp % j == 0 :
            cnt += 1
            tmp //= j
        res = max(res, f(j, cnt))
        if tmp < j : break
    ans.append(res)

print(*ans)