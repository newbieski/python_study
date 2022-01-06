n = int(input())

s = []
b = []

for i in range(n) :
    s.append(input())

for i in range(n) :
    tmp = ""
    for j in range(n) :
        tmp += s[j][i]
    b.append(tmp)

if s == b : print("YES")
else : print("NO")

a=open(0).read().split()[1:]
print('YNEOS'[a!=[''.join(i)for i in zip(*a)]::2])