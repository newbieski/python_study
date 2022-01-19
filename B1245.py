import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
vt = [[False] * m for _ in range(n)]
ans = 0
dyx = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def dfs(y, x, k) :
    if not (0 <= y < n and 0 <= x < m) : return 0
    res = arr[y][x]
    if vt[y][x] or arr[y][x] != k : return res
    vt[y][x] = True
    for dy, dx in dyx :
        ny, nx = y + dy, x + dx
        res = max(res, dfs(ny, nx, k))
    return res

for _ in range(n) :
    s = input().split()
    arr.append([int(i) for i in s])  

for i in range(n) :
    for j in range(m) :
        if vt[i][j] : continue
        tmp = dfs(i, j, arr[i][j])
        if tmp == arr[i][j] : ans += 1
            
print(ans)

n, m = map(int, input().split())
a, b = [], []
ans = 0
for _ in range(n):
	a.append(list(map(int, input().split())))
	b.append([0]*m)
	
def f(i, j):
	b[i][j] = 1
	mov = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
	res = 1
	for k in mov:
		x, y = i+k[0], j+k[1]
		if not (0<=x<n and 0<=y<m) or a[x][y] < a[i][j]:
			continue
		if a[x][y] > a[i][j]:
			res = 0
		elif b[x][y] == 0:
			res = res * f(x, y)
	
	return res
	
print(sum(f(i, j) for i in range(n) for j in range(m) if b[i][j] == 0))