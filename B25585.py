import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
rg = []
n = int(input())
ans = 0
for i in range(n) :
    r = input().split()
    for j in range(n) :
        if r[j] == '1' :
            rg.append((i, j))
        elif r[j] == '2' :            
            rg.insert(0, (i, j))
vt = [False for _ in range(len(rg))]
p = [i for i in range(len(rg))]
def diff(a, b) :
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
def calc() :    
    tmp = 0
    global ans
    for i in range(1, len(rg)) :
        tmp += diff(rg[p[i]], rg[p[i - 1]])
    if ans == 0 or tmp < ans :
        ans = tmp
def recur(k) :    
    if k == len(rg):
        calc()
    else :
        for i in range(1, len(rg)) :
            if not vt[i] :
                vt[i] = True
                p[k] = i
                recur(k + 1)
                vt[i] = False

def sol() :
    b = (rg[0][0] + rg[0][1]) & 1
    for (i, j) in rg[1:] :
        if (i+j) & 1 != b :
            print("Shorei")
            return
    recur(1)
    print("Undertaker")
    print(ans)

sol()


from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
region = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            region.append((i, j))
        if A[i][j] == 2:
            si, sj = i, j

if any((i + j) % 2 != (si + sj) % 2 for i, j in region):
    print("Shorei")
    exit(0)

ans = float("inf")
for perm in permutations(region):
    y, x = si, sj
    t = 0
    for i, j in perm:
        t += max(abs(i - y), abs(j - x))
        y, x = i, j
    ans = min(ans, t)
print("Undertaker")
print(ans)