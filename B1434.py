n, m = map(int, input().split())
a = map(int, input().split())
b = map(int, input().split())
print(sum(a) - sum(b))

g=lambda:sum(map(int,input().split()))
g()
print(g()-g())