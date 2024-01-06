import sys
import math
sys.stdin = open("input.in", "r")
input = sys.stdin.readline
n = int(input())
sum = 0
arr = []
def calc(a, b) :
    d1,d2=a[0]-b[0],a[1]-b[1]
    return math.sqrt(d1*d1+d2*d2)
for i in range(n) :
    x = list(map(int, input().split()))
    for j in range(i) :
        sum += calc(arr[j], x)
    arr.append(x)
print(sum * 2 / n)