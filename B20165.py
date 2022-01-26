import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

n, m, r = map(int, input().split())
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = 0
domi = []
used = [['S'] * m for _ in range(n)]

def isin(y, x) :
    return 0 <= y < n and 0 <= x < m

def attack(y, x, d) :
    global domi, used, ans
    if used[y][x] == 'F' : return

    if d == 'N' : d = 0
    elif d == 'S' : d = 1
    elif d == 'W' : d = 2
    else : d = 3

    cnt = domi[y][x]
    while cnt > 0 and isin(y, x) :        
        if used[y][x] == 'S' :
            used[y][x] = 'F'
            ans += 1
            cnt = max(cnt, domi[y][x])
        y += dy[d]
        x += dx[d]
        cnt -= 1

for _ in range(n) :
    domi.append(list(map(int, input().split())))

for _ in range(r) :
    y, x, d = input().split()
    attack(int(y) - 1, int(x) - 1, d)
    y, x = map(int, input().split())
    used[y - 1][x - 1] = 'S'      

print(ans)
for i in range(n) :
    print(*used[i])    
