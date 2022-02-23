import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.extend(a)
ans = tmp = sum(a[:k])
for i in range(1, n + 1) :
    tmp += a[i + k - 1] - a[i - 1]
    ans = max(ans, tmp)
print(ans)

a=lambda:map(int,input().split())
N,K=a()
P=[*a()]
V=M=sum(P[:K])
for i in range(N):
 V=V-P[i]+P[(i+K)%N]
 M=max(M,V)
print(M)