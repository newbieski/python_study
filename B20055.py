import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

n, k = map(int, input().split())
s, e, step = 0, n - 1, 0
a = list(map(int, input().split()))
rb = [0] * (2 * n)
rbq = []

def plus(p1, p2) : return (n * 2 + p1 + p2) % (n * 2)

def move_conv() :
    global s
    global e
    s = plus(s, -1)
    e = plus(e, -1)
    rb[e] = 0

def release_box(x) : rb[x] = 0

def consume_box(x) :
    if rb[x] == 1 or a[x] == 0 : return False
    a[x] -= 1
    rb[x] = 1
    global k
    if a[x] == 0 : k -= 1
    return True

def move_robot() :
    global rbq
    tmp = []
    for cur in rbq :
        if rb[cur] == 0 : continue
        nxt = plus(cur, 1)
        if consume_box(nxt) :
            release_box(cur)            
            if nxt == e : release_box(nxt)
            else : tmp.append(nxt)
        else : tmp.append(cur)
    rbq = tmp

def upload_robot() :
    if consume_box(s) : rbq.append(s)

while k > 0 :
    step += 1
    move_conv()
    move_robot()
    upload_robot()

    # print(f'[{step}] start {s} end {e} k {k}')
    # print(a)
    # print(rb)
    # print(rbq)
    # print()

print(step)