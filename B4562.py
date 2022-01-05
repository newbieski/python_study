import sys

n = int(input())
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    if a >= b :
        print("MMM BRAINS")
    else :
        print("NO BRAINS")



a = int(input())
for i in range(a):
    a, b = map(int,input().split())
    if a >= b:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')