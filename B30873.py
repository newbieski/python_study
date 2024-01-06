import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
a = 0
for _ in range(int(input())) :
    p,c = map(int, input().split())
    if abs(a-p) <= c :
        a += 1
print(a)