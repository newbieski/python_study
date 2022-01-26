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
