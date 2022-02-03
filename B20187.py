import sys
sys.stdin = open("input.in", "r")
k = int(input())
s = input().split()
h = int(input())

def play(y, x) :    
    ycnt, xcnt = 0, 0
    l, r, u, d = 0, (1<<k) - 1, 0, (1<<k) - 1
    #print("start ", y, x)
    #print(l, r, u, d)
    while l != r or u != d :        
        for e in s :
            if e == 'D' :
                u = (u + d) // 2 + 1
            elif e == 'U' :
                d = (u + d) // 2
            elif e == 'R' :
                l = (l + r) // 2 + 1
            else :
                r = (l + r) // 2
            if y < u :
                ycnt += 1
                y = (u - y - 1) + u
            elif y > d :
                ycnt += 1
                y = d - (y - d - 1)
            elif x < l :
                xcnt += 1
                x = (l - x - 1) + l
            elif x > r :
                xcnt += 1
                x = r - (x - r - 1)
            #print(e, l, r, u, d)
            #print(y, x)
    res = h
    yconv = (2, 3, 0, 1)
    xconv = (1, 0, 3, 2)
    if ycnt % 2 == 1 : res = yconv[res]
    if xcnt % 2 == 1 : res = xconv[res]
    #print(xcnt, ycnt)
    return res

for i in range(1<<k) :
    ans = []
    for j in range(1<<k) :
        ans.append(play(i, j))
    print(*ans)
    