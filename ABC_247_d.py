import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

q = int(input())
dq = []
hd = 0
for _ in range(q) :
    cmd = [*map(int, input().split())]
    if cmd[0] == 1 :
        dq.append([cmd[1], cmd[2]])
    else :
        cnt = cmd[1]
        sum = 0
        while cnt > 0 :
            if dq[hd][1] <= cnt :
                sum += dq[hd][0] * dq[hd][1]
                cnt -= dq[hd][1]
                hd += 1
            else :
                sum += dq[hd][0] * cnt
                dq[hd][1] -= cnt
                cnt = 0
        print(sum)
    
    
