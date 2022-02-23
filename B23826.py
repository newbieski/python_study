import sys

sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
w = []
ans = 0
def dist(x, y) :
    ax, ay = x[:2]
    bx, by = y[:2]
    return abs(ax - bx) + abs(ay - by)
def f(x, y) :
    x, y = w[x], w[y]
    return max(0, x[2] - dist(x, y))
for _ in range(n + 1) :
    w.append(list(map(int, input().split())))

for i in range(1, n + 1) :
    cur = f(0, i)
    for j in range(1, n + 1) :
        cur -= f(j, i)
    ans = max(ans, cur)

if ans : print(ans)
else : print("IMPOSSIBLE")