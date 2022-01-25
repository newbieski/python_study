import sys
input = sys.stdin.readline

stk = [-1]
ans = 0
n = int(input())
for _ in range(n) :
    x, y = map(int, input().split())
    while stk[-1] >= y : 
        if stk[-1] > 0 and stk[-1] != y : ans += 1
        stk.pop()
    stk.append(y)

while stk[-1] > 0 :
    ans += 1
    stk.pop()
print(ans)