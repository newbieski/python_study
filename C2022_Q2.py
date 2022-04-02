import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

tt = int(input())

a = []

def sol(tc) :    
    if sum(a) < 10**6 :
        print(f'Case #{tc}: IMPOSSIBLE')
        return
    x = 10**6
    for i in range(4) :
        if x > a[i] :
            x -= a[i]
        else :
            a[i] = x
            x = 0
    print(f'Case #{tc}:',*a)

for tc in range(tt) :
    a = [10**6 for _ in range(4)]
    for _ in range(3) :
        b = [*map(int, input().split())]
        for i in range(4) :
            a[i] = min(a[i], b[i])
    sol(tc + 1)
