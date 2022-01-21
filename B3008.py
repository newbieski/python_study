import sys
import math
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

n = int(input())
pt = []
count = [dict() for _ in range(n)]
for _ in range(n) :
    pt.append(tuple(map(int, input().split())))

for i in range(n) :
    for j in range(i + 1, n) :
        dx, dy = pt[i][0] - pt[j][0], pt[i][1] - pt[j][1]
        s = 1
        if dx < 0 :
            dx = -dx
            s *= -1
        if dy < 0 :
            dy = -dy
            s *= -1
        if dx == 0 : dy, s = 1, 1
        elif dy == 0 : dx, s = 1, -1
        else :
            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
        res = (dx * s, dy)
        nxt = (dy * s * -1, dx)
        count[i].setdefault(res, 0)
        count[j].setdefault(res, 0)
        count[i][res] += 1
        count[j][res] += 1
        #print(i, j, res)
ans = 0
for i in range(n) :
    for cur in count[i] :
        a, b, = cur
        s = 1
        if a < 0 :
            a, s = -a, -1
        nxt = (b * s * -1, a)
        try :
            ans += count[i][cur] * count[i][nxt]
            #print(i, cur, nxt)
        except:
            continue
        
print(ans // 2)