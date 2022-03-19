import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
tt = int(input())
for _ in range(tt) :
    n = int(input())
    a = list(map(int, input().split()))
    print(min(a), max(a))