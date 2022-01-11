import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
a = []
ee = []
teacher = []

def watch_teacher(k) :
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)    
    for i in range(4) :
        y, x = k
        while 0 <= y < n and 0 <= x < n :
            if a[y][x] == 'S' : return True
            elif a[y][x] == 'O' : break
            y += dy[i]
            x += dx[i]
    return False

def hide() :
    for i in teacher :
        if watch_teacher(i) : return False
    return True    

def brute(s, k) :
    if k == 3 :
        if hide() : return True
        return False
    for i in range(s, len(ee)) :
        y, x = ee[i]
        a[y][x] = 'O'
        if brute(i + 1, k + 1) : return True
        a[y][x] = 'X'
    return False

for i in range(n) :
    a.append(input().split())
    for j in range(n) :
        if a[i][j] == 'T' : teacher.append((i, j))
        elif a[i][j] == 'X' : ee.append((i, j))
        
if brute(0, 0) : print("YES")
else : print("NO")


from itertools import combinations

n = int(input())
graph = []
blank = []
teacher_pos = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
  graph.append(input().split())
  for j in range(n):
    if graph[i][j] == 'T':
      teacher_pos.append((i, j))
    elif graph[i][j] == 'X':
      blank.append((i, j))

for wall in list(combinations(blank, 3)):
  check = True
  for x, y in teacher_pos:
    for i in range(4):
      nx, ny = x, y
      while True:
        nx, ny = nx + dx[i], ny + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx, ny) in wall:
          break
        if graph[nx][ny] == 'S':
          check = False
          break
    if not check:
      break
  if check:
    print('YES')
    break
else:
  print('NO')