import math
s = {0, 1, 2}
#ans = []

def sol(p) :
    global s, ans
    if p in s :
        return
    s.add(p)
    x = int(math.sqrt(p))
    if x * x != p : x += 1
    y = x * x - p
    
    if x < y :
        sol(x)
        sol(y)
    else :
        sol(y)
        sol(x)
    print(x, y)
    #ans.append((x, y))
n = int(input())
sol(n)