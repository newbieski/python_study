import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
u = set()
p = [[] for _ in range(n + 1)]

for _ in range(n) :
    a, b, c, d, e = map(int, input().split())
    p[a] = [b, c, d, e]

ans = []
for i in range(4) :
    a, b = -1, -1
    for j in range(1, n + 1) :
        if j in u : continue
        if p[j][i] > a :
            a, b = p[j][i], j
    if a == -1 : break
    ans.append(b)
    for j in range(4) :
        p[b][j] = -1
print(*ans)

N=int(input())
L=[]
for _ in range(N):L.append([*map(int,input().split()),])
for i in range(1,5):
	j=max(range(len(L)),key=lambda t:(L[t][i],-L[t][0]))
	print(L[j][0],end=' ')
	L.pop(j)