import sys
input = sys.stdin.readline
n = int(input())
d = list(map(int, input().split()))
print((sum(d)+max(d))/2)