import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
tt, k = map(int, input().split())
s1 = [0]
s2 = [0]

def f(x) :
    s = ""
    while x :
        s = str(x % k) + s
        x //= k
    return s

def upper(x, s) :
    l, r = 1, len(s) - 1
    while l < r :
        mid = (l + r) // 2
        if x < s[mid] : r = mid
        else : l = mid + 1
    return l

def sol(n) :
    x = upper(n - 1, s1)
    n -= s1[x - 1]
    x = upper(n - 1, s2)
    n -= s2[x - 1]
    return f(x)[n - 1]

i, sum, tmp = 1, 0, 0
while sum < 2 * (10**9) :
#while sum < 1000 :
    tmp += len(f(i))
    sum += tmp
    i += 1
    s1.append(sum)
    s2.append(tmp)

for _ in range(tt) :
    print(sol(int(input())))
