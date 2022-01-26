import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

n, m, h = map(int, input().split())
mint = []
ans = 0
vt = [False for _ in range(11)]
dist = [[0] * 11 for _ in range(11)]

def brute(prev, hp, cnt) :
    for i in range(1, len(mint)) :
        if vt[i] : continue
        if hp - dist[prev][i] < 0 : continue
        vt[i] = True
        nxthp = hp - dist[prev][i] + h
        if nxthp - dist[i][0] >= 0 :
            global ans
            ans = max(ans, cnt + 1)
        brute(i, nxthp, cnt + 1)
        if ans == len(mint) - 1 : return
        vt[i] = False
    
for i in range(n) :
    row = input().split()
    for j in range(n) :
        if row[j] == '1' : mint.insert(0, (i, j))
        if row[j] == '2' : mint.append((i, j))

for i in range(len(mint)) :
    for j in range(len(mint)) :
        dist[i][j] = abs(mint[i][0] - mint[j][0]) + abs(mint[i][1] - mint[j][1])

brute(0, m, 0)
print(ans)






def dist(A, B):
    ax, ay = A
    bx, by = B
    return abs(ax-bx) +abs(ay-by)

N, M, H = list(map(int,input().split()))
mints = []
s = set()
for n in range(N):
    arr = list(map(int, input().split()))
    for m in range(N):
        if arr[m] == 2:
            mints.append((n,m))
        elif arr[m] == 1:
            house = (n,m)

visit = '0' * len(mints)
s.add((*house, M, 0, visit))
ret = 0
while s:
    nowX, nowY, HP, cnt, visited = s.pop()
    now = (nowX, nowY)
    if cnt > 0 and now == house:
        ret = max(ret, cnt)
        continue
    for i in range(len(mints)):
        if dist(now, mints[i]) <= HP and visited[i] == '0':
            visited = visited[:i] + '1' + visited[i+1:]
            s.add((*mints[i], HP-dist(now, mints[i])+H, cnt+1, visited))
            visited = visited[:i] + '0' + visited[i+1:]
    if not (now == house) and dist(now, house) <= HP :
        s.add((*house, M-dist(now, house), cnt, visited))

print(ret)