import sys
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
c = [i * j for i, j in zip(a, b)]
print(sum(a))
print(sum(a)-sum(c))