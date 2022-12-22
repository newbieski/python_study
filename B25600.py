import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
ans=0
for _ in range(int(input())) :
    a,d,g=[int(i) for i in input().split()]
    tmp = a*(d+g)
    if a == d+g : tmp *= 2
    if ans < tmp : ans = tmp    
print(ans)