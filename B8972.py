import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

r, c = map(int, input().split())
dy = (0, 1, 1, 1, 0, 0, 0, -1, -1, -1)
dx = (0, -1, 0, 1, -1, 0, 1, -1, 0, 1)
ad = []
movecnt = 0

def print_state() :
    ans = [['.'] * c for _ in range(r)]
    y, x = ad[0]
    ans[y][x] = 'I'
    for y, x in ad[1:] :
        ans[y][x] = 'R'
    for s in ans :
        print("".join(s))

def dist(A, B) :
    ay, ax = A
    by, bx = B
    by -= ay
    bx -= ax
    if by < 0 : by = -by
    if bx < 0 : bx = -bx
    return by + bx

def check(A) :
    y, x = A
    return 0 <= y < r and 0 <= x < c

def find_min(A, B) :
    by, bx = B
    R = (0, 0)
    mind = 1000
    for i in range(1, 10) :
        C = (by + dy[i], bx + dx[i])
        if check(C) and dist(A, C) < mind :
            mind = dist(A, C)
            R = C
    return R

def move(dr) :
    global movecnt, ad
    movecnt += 1
    newad = []
    vt = [[0] * c for _ in range(r)]
    y, x = ad[0]
    #print("jongsu ", dr, y, x, " => ", y + dy[dr], x + dx[dr])    
    newad.append((y + dy[dr], x + dx[dr]))
    for i in range(1, len(ad)) :
        y, x = ad[i]
        B = y, x
        if (y, x) == newad[0] : return False
        y, x = find_min(newad[0], (y, x))
        if (y, x) == newad[0] : return False
        vt[y][x] += 1
        newad.append((y, x))
        #print("ad", B, " => ", y, x)
    ad.clear()
    for y, x in newad :
        if vt[y][x] <= 1 : ad.append((y, x))
    return True

for i in range(r) :
    s = input()
    for j in range(c) :
        if s[j] == 'I' :
            ad.insert(0, (i, j))
        elif s[j] == 'R' :
            ad.append((i, j))
#print_state()

cmd = input()
kraj = False
for dr in cmd :
    try:
        if not move(int(dr)) :
            kraj = True
            break
        #print_state()
    except:
        break    

if kraj : print("kraj", movecnt)
else :
    print_state()    
