n = int(input())
a = []
for i in range(n + 1) :
    a.append([0, i])
x = map(int, input().split())
for i in x :
    if i : a[i][0] += 1
a.sort(reverse = True)
if (a[0][0] == a[1][0]) : print("skipped")
else : print(a[0][1])

N=int(input())
a=[0]*N
for i in map(int, input().split()):
    if i:
        a[i-1]+=1
b=max(a)
if a.count(b)>1:
    print('skipped')
else:
    print(1+a.index(b))