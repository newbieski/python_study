import sys
import math

t = int(input())

for _ in range(t) :
    m, p, a, b = map(int, input().split())    
    x = (a * b + m) // (a + 1)
    y = a * x - a * b
    z = m - x - y
    ans = math.pow(a, p//2) * x + math.pow(1/a, p//2) * y
    if z > 1 :
        q = math.sqrt(a)    
        ans += math.pow(q/z*(z-1), p) + math.pow(q/z,p)*(z-1)
    print(round(ans))

