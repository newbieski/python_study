import math
MOD = 10**9+7
n=int(input())
a,b=map(int,input().split())
sum=0
prev = 0
for i in range(1, n + 1) :
    sum += prev + i * (n - i)
    prev = i * (n - i)
p, q = sum * pow((b - a), 3), 2 * pow(n, 3)
g = math.gcd(p, q)
p, q = p//g, q//g
print(p*pow(q, MOD-2, MOD)%MOD)
