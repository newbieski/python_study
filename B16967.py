import sys
sys.stdin = open('input.in', 'r')
input = sys.stdin.readline
h,w,x,y = map(int, input().split())
b = []
a = [[0]*w for _ in range(h)]
check = [[0]*(w+y) for _ in range(h + x)]
for i in range(h) :
    for j in range(w) :
        check[i][j] += 1
        check[i + x][j + y] += 1
for _ in range(h + x) :
    b.append(list(map(int, input().split())))
for i in range(h) :
    for j in range(w) :
        a[i][j] = b[i][j]
        if check[i][j] == 2 : a[i][j] -= a[i - x][j - y]
for row in a :
    print(" ".join([str(x) for x in row]))