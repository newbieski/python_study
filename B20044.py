n = int(input())
a = list(map(int, input().split()))
a.sort()
b = a[n:]
b.reverse()
c = [x + y for x, y in zip(a[:n], b)]
print(min(c))


n = int(input())
arr = sorted(map(int,input().split()))
print(min(arr[i]+arr[~i] for i in range(2*n)))