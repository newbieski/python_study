n = int(input())
a = []
a.append(int(input()))
for i in range(n - 1) :
    c = input()
    b = int(input())
    if c == '+' or c == '-' :
        a.append(c)
        a.append(b)
    if c == '/' :
        a[-1] //= b
    if c == '*' :
        a[-1] *= b
ans = a[0]
for i in range(1, len(a), 2) :
    if a[i] == '+' :
        ans += a[i + 1]
    else :
        ans -= a[i + 1]
print(ans)

s=''
for _ in range(int(input())*2-1):
	s+=input()
print(eval(s.replace('/','//')))