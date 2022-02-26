import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
p,q,r,s = map(int, input().split())
tot = sum(a)
x = [1]
for i in a :
    if i - r > 0 : x.append(i - r)
    x.append(i + 1)
x.sort()

def f() :
    cur = tot - n * p
    i, j = 0, 0
    for k in x :
        while j < n and a[j] <= k + r :
            cur += p
            j += 1
        while i < n and a[i] < k :
            cur += q
            i += 1
        if cur >= s : return k
    return -1

print(f())