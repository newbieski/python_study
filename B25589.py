import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
a = []
a.append([0 for _ in range(n + 1)])
subsum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(n) :
    tmp = [0]
    tmp.extend(list(map(int, input().split())))    
    a.append(tmp)
for i in range(1, n + 1) :
    tmp = 0
    for j in range(1, n + 1) :
        tmp +=a[i][j]
        subsum[i][j] = subsum[i - 1][j] + tmp        

def sum(ay, ax, by, bx) :
    return subsum[by][bx] - subsum[by][ax - 1] - subsum[ay - 1][bx] + subsum[ay - 1][ax - 1]

leftvert = [0 for _ in range(n + 2)]
rightvert = [0 for _ in range(n + 2)]
uphorz = [0 for _ in range(n + 2)]
downhorz = [0 for _ in range(n + 2)]

def calc_leftvert() :
    for x in range(1, n + 1) :
        leftvert[x] = leftvert[x - 1]
        for y in range(1, n + 1) :
            for sz in range(1, n + 1) :
                ay, ax = y - sz + 1, x - sz + 1
                by, bx = y, x
                if ay < 1 or ax < 1 :
                    break
                leftvert[x] = max(leftvert[x], sum(ay, ax, by, bx) - sz**4)        
        

def calc_rightvert() :    
    for x in range(n, 0, -1) :
        rightvert[x] = rightvert[x + 1]
        for y in range(1, n + 1) :
            for sz in range(1, n + 1) :
                ay, ax = y, x
                by, bx = y + sz - 1, x + sz - 1                
                if n < by or n < bx :
                    break                
                rightvert[x] = max(rightvert[x], sum(ay, ax, by, bx) - sz**4)        

def calc_uphorz() :    
    for y in range(1, n + 1) :
        uphorz[y] = uphorz[y - 1]    
        for x in range(1, n + 1) :
            for sz in range(1, n + 1) :
                ay, ax = y - sz + 1, x - sz + 1
                by, bx = y, x
                if ay < 1 or ax < 1 :
                    break
                uphorz[y] = max(uphorz[y], sum(ay, ax, by, bx) - sz**4)
        
def calc_downhorz() :    
    for y in range(n, 0, -1) :
        downhorz[y] = downhorz[y + 1]        
        for x in range(1, n + 1) :
            for sz in range(1, n + 1) :
                ay, ax = y, x
                by, bx = y + sz - 1, x + sz - 1
                if n < by or n < bx :
                    break
                downhorz[y] = max(downhorz[y], sum(ay, ax, by, bx) - sz**4)        
            
calc_leftvert()
calc_rightvert()
calc_uphorz()
calc_downhorz()
ans = 0
for i in range(1, n) :
    ans = max(ans, leftvert[i] + rightvert[i + 1])
    ans = max(ans, uphorz[i] + downhorz[i + 1])
print(ans)
