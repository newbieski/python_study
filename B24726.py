import math
x1,y1,x2,y2,x3,y3=map(int, input().split())
p = [(x1, y1), (x2, y2), (x3, y3)]
q = [(y1, x1), (y2, x2), (y3, x3)]
p.sort()
q.sort()

def calc(p1, p2) :
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 : return 0
    if y1 == y2 : return math.pi * y1 * y1 * abs(x1 - x2)
    a, b, d = max(y1, y2), min(y1, y2), abs(x1-x2)
    h = a*d/(a-b)
    return math.pi / 3 * (a * a * h - b * b * (h - d))
ans1 = calc(p[0], p[1]) + calc(p[1], p[2]) - calc(p[0], p[2])
ans2 = calc(q[0], q[1]) + calc(q[1], q[2]) - calc(q[0], q[2])
print(abs(ans1), abs(ans2))


from math import pi
x1, y1, x2, y2, x3, y3 = map(int, input().split())
S = abs(x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3) / 2
x, y = (x1+x2+x3)/3, (y1+y2+y3)/3
print(2*pi*y*S, 2*pi*x*S)