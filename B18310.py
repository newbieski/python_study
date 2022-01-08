import sys
input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
print(a[(n - 1)//2])