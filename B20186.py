import sys
input = sys.stdin.readline
n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(n - k) :
    a[i] = 0
print(sum(a) - k * (k - 1) // 2)

n,k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
print(sum(nums[-k:]) - ((k-1)**2 + (k-1))//2)