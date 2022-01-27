import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
w = []
ans = 1000000
for _ in range(n) :
    s, t = map(int, input().split())
    w.append((t, s))
w.sort(reverse=True)
for t, s in w :
    if t < ans : ans = t
    ans -= s
if ans < 0 : ans = -1
print(ans)