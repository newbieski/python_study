import sys
sys.stdin=open("input.in", "r")
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
tr=[[0, []], [0, []]]
def update(x) :
    cur = tr
    for i in range(30, -1, -1) :
        w = 0
        if (x & (1<<i)) > 0 :
            w = 1
        if cur[w][0] == 0 :
            cur[w][1] = [[0, []], [0, []]]
        cur[w][0] += 1
        cur = cur[w][1]
    
def delete(x) :
    cur = tr
    for i in range(30, -1, -1) :
        w = 0
        if (x & (1<<i)) > 0 :
            w = 1
        cur[w][0] -= 1
        cur = cur[w][1]

def find(k, x) :
    cur = tr
    res = 0
    for i in range(30, -1, -1) :
        w = 0
        if (x & (1<<i)) == 0 :
            w = 1
        if cur[w][0] < k :
            k -= cur[w][0]
            w ^= 1
        if w > 0 :
            res += (1<<i)        
        cur = cur[w][1]
    return res
for x in a :    
    update(x)

for _ in range(int(input())) :
    c,k,x = map(int, input().split())
    if c == 1 :
        k -= 1
        delete(a[k])
        update(x)
        a[k] = x
    if c == 2 :
        print(find(k, x)^x)