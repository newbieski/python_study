s = list(map(int, input().split()))
a = min(s)
abc = max(s)
s.pop(s.index(a))
s.pop(s.index(abc - a))
s.pop(s.index(abc))
b = min(s)
print(a, b, abc - a - b)

s=sorted(map(int,input().split()))
print(s[0],s[1],s[4]-s[0])