import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
t = int(input())

"""
def numsum(a) :
    res = 0
    while a :
        res += a % 10
        a //= 10
    return res

def brutesum(a, b) :
    res = 0
    for i in range(a, b + 1) :
        res += numsum(i)
    return res
"""


def fastsum(k) :
    return 45 * (10 ** (k - 1)) * k

def calc(x) :
    if x < 10 :
        return x * (x + 1) // 2
    s = str(x)
    d = len(s)
    res = fastsum(d - 1)
    mod = 10 ** (d - 1)
    for i in range(1, int(s[0])) :
        res += i * mod
        res += fastsum(d - 1)
    x %= mod
    res += int(s[0]) * (x + 1)

    return res + calc(x)

    return res
while t > 0 :
    t -= 1
    a, b = map(int, input().split())
    if a > 0 : a -= 1
    print(calc(b) - calc(a))
    
    
    
