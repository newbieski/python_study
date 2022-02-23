import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
MOD = 10**9+7
n = int(input())
a = list(map(int, input().split()))
ans, sum = 0, 0
for i in a :
    ans += i * sum
    ans %= MOD
    sum += i
    sum %= MOD
print(ans)

n=int(input())
a=list(map(int,input().split()))
m=10**9+7
p,A=0,0
for i in range(n):
    A+=p*a[i]%m
    p+=a[i]
print(A%m)