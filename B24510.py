import sys
input = sys.stdin.readline
n = int(input())
ans = 0

def f(str, key) :
    p = 0
    sum = 0
    while 1 :
        p = str.find(key, p)
        if p == -1 : break
        sum += 1
        p += len(key)
    return sum

for _ in range(n) :
    s = input()    
    ans = max(ans, f(s, "for") + f(s, "while"))
print(ans)
