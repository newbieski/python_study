import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline

tt = int(input())

def sol(a) :
    cur = 1
    for i in a :
        if i >= cur :
            cur += 1
    return cur - 1

for tc in range(tt) :
    n = int(input())
    a = sorted(map(int, input().split()))
    print(f'Case #{tc + 1}: {sol(a)}')